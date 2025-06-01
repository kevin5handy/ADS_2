import joblib
import numpy as np
import pandas as pd

# Data

encoder_Application_mode = joblib.load("model/encoder_Application_mode.joblib")
encoder_Course = joblib.load("model/encoder_Course.joblib")
encoder_Daytime_evening_attendance = joblib.load("model/encoder_Daytime_evening_attendance.joblib")
encoder_Debtor = joblib.load("model/encoder_Debtor.joblib")
encoder_Displaced = joblib.load("model/encoder_Displaced.joblib")
encoder_Educational_special_needs = joblib.load("model/encoder_Educational_special_needs.joblib")
encoder_Fathers_occupation = joblib.load("model/encoder_Fathers_occupation.joblib")
encoder_Fathers_qualification = joblib.load("model/encoder_Fathers_qualification.joblib")
encoder_Gender = joblib.load("model/encoder_Gender.joblib")
encoder_International = joblib.load("model/encoder_International.joblib")
encoder_Marital_status = joblib.load("model/encoder_Marital_status.joblib")
encoder_Mothers_occupation = joblib.load("model/encoder_Mothers_occupation.joblib")
encoder_Mothers_qualification = joblib.load("model/encoder_Mothers_qualification.joblib")
encoder_Nacionality = joblib.load("model/encoder_Nacionality.joblib")
encoder_Previous_qualification = joblib.load("model/encoder_Previous_qualification.joblib")
encoder_Scholarship_holder = joblib.load("model/encoder_Scholarship_holder.joblib")
encoder_Tuition_fees_up_to_date =joblib.load("model/encoder_Tuition_fees_up_to_date.joblib")
pca_1 = joblib.load("model/pca_1.joblib")
scaler_Admission_grade = joblib.load("model/scaler_Admission_grade.joblib")
scaler_Age_at_enrollment = joblib.load("model/scaler_Age_at_enrollment.joblib")
scaler_Application_order = joblib.load("model/scaler_Application_order.joblib")
scaler_Curricular_units_1st_sem_approved = joblib.load("model/scaler_Curricular_units_1st_sem_approved.joblib")
scaler_Curricular_units_1st_sem_credited = joblib.load("model/scaler_Curricular_units_1st_sem_credited.joblib")
scaler_Curricular_units_1st_sem_enrolled = joblib.load("model/scaler_Curricular_units_1st_sem_enrolled.joblib")
scaler_Curricular_units_1st_sem_evaluations = joblib.load("model/scaler_Curricular_units_1st_sem_evaluations.joblib")
scaler_Curricular_units_1st_sem_grade = joblib.load("model/scaler_Curricular_units_1st_sem_grade.joblib")
scaler_Curricular_units_1st_sem_without_evaluations = joblib.load("model/scaler_Curricular_units_1st_sem_without_evaluations.joblib")
scaler_Curricular_units_2nd_sem_approved = joblib.load("model/scaler_Curricular_units_2nd_sem_approved.joblib")
scaler_Curricular_units_2nd_sem_credited = joblib.load("model/scaler_Curricular_units_2nd_sem_credited.joblib")
scaler_Curricular_units_2nd_sem_enrolled = joblib.load("model/scaler_Curricular_units_2nd_sem_enrolled.joblib")
scaler_Curricular_units_2nd_sem_evaluations = joblib.load("model/scaler_Curricular_units_2nd_sem_evaluations.joblib")
scaler_Curricular_units_2nd_sem_grade = joblib.load("model/scaler_Curricular_units_2nd_sem_grade.joblib")
scaler_Curricular_units_2nd_sem_without_evaluations = joblib.load("model/scaler_Curricular_units_2nd_sem_without_evaluations.joblib")
scaler_GDP = joblib.load("model/scaler_GDP.joblib")
scaler_Inflation_rate = joblib.load("model/scaler_Inflation_rate.joblib")
scaler_Previous_qualification_grade = joblib.load("model/scaler_Previous_qualification_grade.joblib")
scaler_Unemployment_rate = joblib.load("model/scaler_Unemployment_rate.joblib")

pca_numerical_columns = [
    'Curricular_units_1st_sem_credited',
    'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_evaluations',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Curricular_units_2nd_sem_credited',
    'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_evaluations',
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade'
]

# Contoh dengan try-except dan penanganan input Series yang berisi string tunggal
def data_preprocessing(data_input):
    st.write("--- Memulai data_preprocessing ---") # Untuk debug di UI jika file ini diimport ke app.py
    print("--- Memulai data_preprocessing ---")   # Untuk debug di terminal

    data_copied = data_input.copy()
    df_processed = pd.DataFrame(index=[0]) # Inisialisasi dengan satu baris indeks

    # Daftar kolom sesuai urutan X_train di notebook
    expected_training_columns = [
        'Marital_status', 'Application_mode', 'Application_order', 'Course', 'Daytime_evening_attendance',
        'Previous_qualification', 'Previous_qualification_grade', 'Nacionality', 'Mothers_qualification',
        'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation', 'Admission_grade', 
        'Displaced', 'Educational_special_needs', 'Debtor', 'Tuition_fees_up_to_date', 'Gender', 
        'Scholarship_holder', 'Age_at_enrollment', 'International', 'Curricular_units_1st_sem_without_evaluations',
        'Curricular_units_2nd_sem_without_evaluations', 'Unemployment_rate', 'Inflation_rate', 'GDP',
        'pc1_1', 'pc1_2', 'pc1_3', 'pc1_4', 'pc1_5'
    ] # Total 31 kolom contoh

    # --- Encoding Kolom Kategorikal ---
    categorical_features_app_order = [ # Sesuaikan urutan ini jika nama kolomnya berbeda sedikit
        ("Application_mode", encoder_Application_mode), ("Course", encoder_Course),
        ("Daytime_evening_attendance", encoder_Daytime_evening_attendance), ("Debtor", encoder_Debtor),
        ("Displaced", encoder_Displaced), ("Educational_special_needs", encoder_Educational_special_needs),
        ("Fathers_occupation", encoder_Fathers_occupation), ("Fathers_qualification", encoder_Fathers_qualification),
        ("Gender", encoder_Gender), ("International", encoder_International),
        ("Marital_status", encoder_Marital_status), ("Mothers_occupation", encoder_Mothers_occupation),
        ("Mothers_qualification", encoder_Mothers_qualification), ("Nacionality", encoder_Nacionality),
        ("Previous_qualification", encoder_Previous_qualification), ("Scholarship_holder", encoder_Scholarship_holder),
        ("Tuition_fees_up_to_date", encoder_Tuition_fees_up_to_date)
    ]

    for col_name, encoder in categorical_features_app_order:
        try:
            # Asumsi data_copied[col_name] adalah Series berisi satu string dari st.selectbox
            # atau jika sudah jadi DataFrame dengan 1 baris, data_copied[col_name].iloc[0] adalah stringnya
            input_string = str(data_copied[col_name].iloc[0])
            df_processed[col_name] = encoder.transform([input_string])[0]
            print(f"Encoding {col_name}: '{input_string}' -> {df_processed[col_name].iloc[0]}")
        except Exception as e:
            print(f"Error encoding {col_name} dengan input '{data_copied[col_name].iloc[0]}': {e}")
            df_processed[col_name] = np.nan # Atau nilai default lain

    # --- Scaling Kolom Numerik ---
    numerical_features_app_order = [ # Sesuaikan urutan dan nama
        ("Admission_grade", scaler_Admission_grade), ("Age_at_enrollment", scaler_Age_at_enrollment),
        ("Application_order", scaler_Application_order),
        ("Curricular_units_1st_sem_without_evaluations", scaler_Curricular_units_1st_sem_without_evaluations),
        ("Curricular_units_2nd_sem_without_evaluations", scaler_Curricular_units_2nd_sem_without_evaluations),
        ("GDP", scaler_GDP), ("Inflation_rate", scaler_Inflation_rate),
        ("Previous_qualification_grade", scaler_Previous_qualification_grade),
        ("Unemployment_rate", scaler_Unemployment_rate)
    ]

    for col_name, scaler in numerical_features_app_order:
        try:
            # Asumsi data_copied[col_name] adalah Series berisi satu angka dari st.number_input
            input_value = data_copied[col_name].iloc[0]
            df_processed[col_name] = scaler.transform(np.asarray([[input_value]]))[0] # reshape jadi [[value]]
            print(f"Scaling {col_name}: {input_value} -> {df_processed[col_name].iloc[0]}")
        except Exception as e:
            print(f"Error scaling {col_name} dengan input '{data_copied[col_name].iloc[0]}': {e}")
            df_processed[col_name] = np.nan


    # --- PCA ---
    # pca_numerical_columns sudah didefinisikan di level modul
    try:
        # Buat DataFrame sementara untuk input PCA, pastikan kolomnya di-scale
        pca_input_df = pd.DataFrame(index=[0])
        for col_pca in pca_numerical_columns:
            # Ambil scaler yang sesuai dari global(). Namanya harus konsisten.
            # Contoh: scaler_Curricular_units_1st_sem_credited
            scaler_pca_col = globals()[f"scaler_{col_pca}"] # Ambil objek scaler berdasarkan nama string
            input_value_pca = data_copied[col_pca].iloc[0]
            pca_input_df[col_pca] = scaler_pca_col.transform(np.asarray([[input_value_pca]]))[0]

        pca_components = pca_1.transform(pca_input_df[pca_numerical_columns]) # Input harus DataFrame dengan kolom yg benar
        
        pca_component_names = [f"pc1_{i+1}" for i in range(pca_components.shape[1])]
        df_processed[pca_component_names] = pca_components[0] # Ambil baris pertama dari hasil PCA
        print(f"PCA components: {pca_components[0]}")

    except Exception as e:
        print(f"Error saat PCA: {e}")
        for i in range(1, 6): # Asumsi 5 komponen
             df_processed[f"pc1_{i}"] = np.nan

    # Pastikan urutan kolom df_processed sama dengan expected_training_columns
    try:
        df_processed = df_processed[expected_training_columns]
    except Exception as e:
        print(f"Error saat reordering kolom di df_processed: {e}")
        st.error("Gagal menyusun ulang kolom akhir. Periksa daftar 'expected_training_columns'.")
        # Mungkin kembalikan df_processed apa adanya atau None jika kritis
        # return None

    print("--- Selesai data_preprocessing, mengembalikan df_processed ---")
    return df_processed
