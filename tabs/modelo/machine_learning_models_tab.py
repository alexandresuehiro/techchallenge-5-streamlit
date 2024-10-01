import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, mean_squared_error
import streamlit as st
import csv
import os
from tabulate import tabulate
from tabs.tab import TabInterface


class ModelosMachineLearningTab(TabInterface):
    df: pd.DataFrame

    def __init__(self, tab):
        self.tab = tab

        uploaded_file = "data/dataset.csv"

        if uploaded_file is not None:
            #df = pd.read_csv(uploaded_file)
            df_load = pd.read_csv(uploaded_file, sep=';', encoding='UTF-8-SIG') #, engine='python')
            df = self.data_cleaning(df_load)

        self.render(df)

    def data_cleaning(self, df):
            for col in [col for col in df.columns if col.endswith('_INT')]:
              # Convert to float first, handling non-finite values with 'coerce'
              #df[col] = pd.to_numeric(df[col], errors='coerce')
              df[col] = df[col].astype(str).str.replace('.0', '', regex=False).replace('nan', '')
              df[col] = pd.to_numeric(df[col], errors='coerce') # convert the column to numeric type, coerce will replace invalid parsing as NaN
              # Now convert to integer, filling NaNs with a suitable value (e.g., -1)
              df[col] = df[col].fillna(0).astype(float)
              df[col] = df[col].fillna('')

            for col in [col for col in df.columns if col.endswith('_NUM')]:
              # Convert column to string type
              df[col] = df[col].astype(str)
              # Replace '#NULO!' and 'nan' with empty strings
              df[col] = df[col].str.replace('#NULO!', '').str.replace('nan', '')
              # Convert column to float type, non-numeric values will be converted to NaN
              df[col] = pd.to_numeric(df[col], errors='coerce') # use pd.to_numeric with errors='coerce' to handle invalid parsing
              # Fill NaN values with 0 and convert to float type
              df[col] = df[col].fillna(0).astype(float)
              df[col] = df[col].fillna('')

            for col in [col for col in df.columns if col.endswith('_DATE')]:
              # Convert the column to string type
              df[col] = df[col].astype(str)
              # Replace 'nan' with empty string
              df[col] = df[col].str.replace('nan', '')
              # Convert the column to numeric type, coerce will replace invalid parsing as NaN
              df[col] = pd.to_numeric(df[col], errors='coerce')
              # Convert to datetime objects with year format, handling errors
              df[col] = pd.to_datetime(df[col], format='%Y', errors='coerce').dt.year
              # Fill NaN with 0 and convert to int
              df[col] = df[col].fillna(0).astype(int)
              # Remove '.0' from the year values
              df[col] = df[col].astype(str).str.replace('.0', '', regex=False)
              df[col] = df[col].fillna('')

            for col in [col for col in df.columns if col.endswith('_STR')]:
              df[col] = df[col].str.replace('#NULO!', '').str.replace('nan', '')
              df[col] = df[col].fillna('')

            for col in [col for col in df.columns if col.startswith('IDADE')]:
              # Convert the column to string type
              df[col] = df[col].astype(str)
              # Replace 'nan' with empty string
              df[col] = df[col].str.replace('nan', '')
              # Convert the column to float type, coerce will replace invalid parsing as NaN
              df[col] = pd.to_numeric(df[col], errors='coerce') # Use errors='coerce' to handle invalid parsing
              # Convert the column to integer type
              df[col] = df[col].fillna(0).astype('int') # Fill NaN with 0 and convert to int
              df[col] = df[col].fillna('')

            return df

    def generate_patterns_list(self, df):
        # Define your patterns
        pattern1 = r'^IPP.*NUM'   # Pattern 1
        pattern2 = r'^IEG.*_NUM'  # Pattern 2
        pattern3 = r'^I.*_NUM'    # Pattern 3

        # Combine patterns using the '|' operator
        combined_pattern = f"({pattern1})|({pattern2})|({pattern3})"  # Using f-string for readability

        # Filter columns using the combined pattern
        features = df.filter(regex=combined_pattern).columns.tolist()

        pattern1 = r'^PONTO.*STR'  # Pattern 1
        pattern2 = r'^NIVEL.*_STR'   # Pattern 2
        pattern3 = r'^IND.*'       # Pattern 3

        # Combine patterns using the '|' operator
        combined_pattern = f"({pattern1})|({pattern2})|({pattern3})"  # Using f-string for readability

        # Filter columns using the combined pattern
        target = df.filter(regex=combined_pattern).columns.tolist()

        return features, target

    @st.cache
    def predict_success(self, df, features, target, model_type, test_size=0.2, random_state=42):
          """
          Predizer sucesso usando modelos de classificação ou regressão.

          Args:
            df: Pandas DataFrame contendo os dados.
            features: List of column names to be used as features.
            target: Column name to be used as the target variable.
            model_type: Type of model to use ('classification' or 'regression').
            test_size: Proportion of data to use for testing (default: 0.2).
            random_state: Random seed for reproducibility (default: 42).

          Returns:
            A dictionary containing the trained model, accuracy/MSE score, predictions,
            and a DataFrame with 'NOME' and index for successful and unsuccessful predictions.
          """

          threshold = 0.1  # Threshold for regression predictions

          # 1. Drop rows with nulls or empty strings in features OR target
          df_cleaned = df.dropna(subset=features + [target])  # Drop if missing in any feature or target
          df_cleaned = df_cleaned[~df_cleaned[features + [target]].eq('').any(axis=1)]  # Drop if empty string in any feature or target

          df_dropna = df_cleaned

          # Check if there's any data left after filtering
          if df_cleaned.empty:
                return "Not enough data with complete feature and target values for prediction."
          

          df_cleaned[target] = df_cleaned[target].str.replace('Não', '0')
          df_cleaned[target] = df_cleaned[target].str.replace('Sim', '1').astype(int)

          # 2. Split data into training and testing sets
          X = df_cleaned[features]
          y = df_cleaned[target]

          
          X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
            
          # Choose model based on model_type: 
          # Classification: Logistic Regression, Decision Tree - Classification, Random Forest - Classification
          # Regression: Linear Regression, Decision Tree - Regression, Random Forest - Regression
          if model_type == 'Logistic Regression':
            models = {
                'Logistic Regression': LogisticRegression(random_state=random_state)
            }
          elif model_type == 'Decision Tree - Classification':
            models = {
                'Decision Tree - Classification': DecisionTreeClassifier(random_state=random_state)
            }
          elif model_type == 'Random Forest - Classification':
            models = {
                'Random Forest - Classification': RandomForestClassifier(random_state=random_state)
                }
          elif model_type == 'Linear Regression':
            models = {
                'Linear Regression': LinearRegression()
            }
          elif model_type == 'Decision Tree - Regression':
            models = {
                'Decision Tree - Regression': DecisionTreeRegressor(random_state=random_state)
          
            }
          elif model_type == 'Random Forest - Regression':
            models = {
                'Random Forest - Regression': RandomForestRegressor(random_state=random_state)
          }
          else:
            return f"Invalid model type. Please choose:\n'Logistic Regression' or \n'Decision Tree - Classification' or \n'Random Forest - Classification' or \n'Linear Regression' or \n'Decision Tree - Regression' or \n'Random Forest - Regression' or \n'regression'."


          results = {}
          for model_name, model in models.items():
            # Train the model
            model.fit(X_train, y_train)

            # Make predictions
            predictions = model.predict(X_test)

            sorted_predictions_df = pd.DataFrame()  # Initialize here


        # Evaluate the model and get indices
            if model_type == 'Logistic Regression' or model_type == 'Decision Tree - Classification' or model_type == 'Random Forest - Classification':
              score = accuracy_score(y_test, predictions)

            # Create a DataFrame with 'NOME' and index for successful predictions
              successful_df = df_dropna.loc[X_test[y_test == predictions].index, ['NOME_STR']].copy()
              successful_df['Index'] = successful_df.index
              successful_df.rename(columns={'NOME_STR': 'NOME'}, inplace=True)
              # Filter out empty strings in 'NOME' column
              successful_df = successful_df[successful_df['NOME'] != ''] 

              # Create a DataFrame with 'NOME' and index for unsuccessful predictions
              unsuccessful_df = df_dropna.loc[X_test[y_test != predictions].index, ['NOME_STR']].copy()
              unsuccessful_df['Index'] = unsuccessful_df.index
              unsuccessful_df.rename(columns={'NOME_STR': 'NOME'}, inplace=True)
              # Filter out empty strings in 'NOME' column
              unsuccessful_df = unsuccessful_df[unsuccessful_df['NOME'] != ''] 

            else:
              score = mean_squared_error(y_test, predictions)
                
              # Create a DataFrame with 'NOME', index, and predictions
              prediction_df = df_dropna.loc[X_test.index, ['NOME_STR']].copy() # Use X_test.index to get the original index
              prediction_df['Index'] = prediction_df.index
              prediction_df['Prediction'] = predictions  
              prediction_df.rename(columns={'NOME_STR': 'NOME'}, inplace=True)

              # Sort by prediction values (descending for "bigger is better")
              sorted_predictions_df = prediction_df.sort_values(by=['Prediction'], ascending=False)

              # Create a DataFrame with 'NOME' and index for successful predictions
              successful_df = df_dropna.loc[X_test[abs(y_test - predictions) <= threshold].index, ['NOME_STR']].copy()
              successful_df['Index'] = successful_df.index
              successful_df.rename(columns={'NOME_STR': 'NOME'}, inplace=True)

              # Create a DataFrame with 'NOME' and index for unsuccessful predictions
              unsuccessful_df = df_dropna.loc[X_test[abs(y_test - predictions) > threshold].index, ['NOME_STR']].copy()
              unsuccessful_df['Index'] = unsuccessful_df.index
              unsuccessful_df.rename(columns={'NOME_STR': 'NOME'}, inplace=True)

          results[model_name] = {'model': model, 'score': score, 'predictions': predictions,
                                       'successful_df': successful_df, 'unsuccessful_df': unsuccessful_df,
                                       'sorted_predictions_df': sorted_predictions_df} # Add sorted predictions to results

          return results

    def get_file_type(self, file_path):
          """Returns the file type of a file.
          """
          extension = os.path.splitext(file_path)[1].lower()
          if extension == '.csv':
            return 'csv'
          elif extension == '.txt':
            return 'txt'
          elif extension == '.zip':
            return 'zip'
          else:
            return 'unknown'


    # Streamlit app
    #st.title("Predição de Sucesso por Machine Learning")
    def render(self, df):

        with self.tab:
            st.subheader(":blue[Sobre do modelo]", divider="blue")

            st.markdown(
                """
                Este conjunto analisa a base de dados a partir de um modelo de Machine Learning.
            """
            )

            st.subheader(":blue[Performance do modelo]", divider="blue")

        features, target = self.generate_patterns_list(df)

        # Feature and target selection
        st.header("Selecionar Features e Target")
        all_columns = features
        features = st.multiselect("Features", all_columns)
        target = st.selectbox("Target", target)

        # Model selection
        st.header("Selecionar Modelo")
        model_type = st.selectbox(
            "Model Type",
            [
                "Logistic Regression",
                "Decision Tree - Classification",
                "Random Forest - Classification",
                "Linear Regression",
                "Decision Tree - Regression",
                "Random Forest - Regression",
            ],
        )

        # Run prediction
        if st.button("Predição"):
            results = self.predict_success(self.df, features, target, model_type)

            # Display results
            if isinstance(results, str):  # Handle error message
                st.error(results)
            else:
                table_rows = []
                for model_name, data in results.items():
                    successful_count = len(data['successful_df'])
                    unsuccessful_count = len(data['unsuccessful_df'])
                    table_rows.append([model_name, data['score'], successful_count, unsuccessful_count])


                st.subheader("Tipo de Modelo: ")
                st.code(model_name)

                st.subheader("Score")
                st.code(data['score'])

                col1, col2 = st.columns(2)
                with col1:
                        st.subheader(f"Predição de Sucesso\nTotal: {successful_count}")
                        st.dataframe(results[model_type]['successful_df'])
                with col2:
                        st.subheader(f"Predição de Falha\nTotal: {unsuccessful_count}")
                        st.dataframe(results[model_type]['unsuccessful_df'])

