# Di dalam file data_preprocessing.py
import pandas as pd
import numpy as np # Pastikan numpy diimpor untuk np.nan
import streamlit as st # Tambahkan ini jika belum ada, untuk st.write di dalam fungsi ini
import joblib

# ... (load semua encoder dan scaler Anda seperti biasa) ...
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
rdf_model = joblib.load("model/rdf_model.joblib")
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
tree_model = joblib.load("model/tree_model.joblib")

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

def data_preprocessing(data_input):
    st.write("--- Memulai data_preprocessing ---") # Output akan muncul di UI Streamlit
    print("--- Memulai data_preprocessing ---")   # Output akan muncul di terminal

    data_copied = data_input.copy()
    df_processed = pd.DataFrame()

    # --- DEBUGGING DETAIL UNTUK SATU KOLOM KATEGORIKAL (MISALNYA APPLICATION_MODE) ---
    target_column_name = "Application_mode"
    encoder_object = encoder_Application_mode # Gunakan encoder yang sesuai

    st.subheader(f"🔍 Debug Detail untuk: {target_column_name}") # Judul di UI
    print(f"\n🔍 Debug Detail untuk: {target_column_name}")

    try:
        input_value_list = data_copied[target_column_name] # Ini adalah list, misal: ['Nilai String dari Selectbox']
        st.write(f"Input '{target_column_name}' (dari data_copied): `{input_value_list}`")
        print(f"Input '{target_column_name}' (dari data_copied): {input_value_list}")

        if not input_value_list or input_value_list[0] is None:
            st.warning(f"Input untuk '{target_column_name}' kosong atau None!")
            print(f"WARNING: Input untuk '{target_column_name}' kosong atau None!")
            encoded_value_scalar = np.nan
        else:
            actual_string_to_transform = input_value_list[0] # String sebenarnya
            st.write(f"String aktual yang akan di-transform: `'{actual_string_to_transform}'` (Tipe: `{type(actual_string_to_transform)}`)")
            print(f"String aktual yang akan di-transform: '{actual_string_to_transform}' (Tipe: {type(actual_string_to_transform)})")

            # Tampilkan beberapa kelas yang diketahui encoder untuk perbandingan
            known_classes = list(encoder_object.classes_)
            st.write(f"Beberapa kelas yang diketahui encoder '{target_column_name}' (total {len(known_classes)}): `{known_classes[:20]}` ...") # Tampilkan 20 kelas pertama
            print(f"Kelas yang diketahui encoder '{target_column_name}': {known_classes}")

            # Cek apakah string ada di dalam kelas encoder
            is_known = actual_string_to_transform in known_classes
            st.write(f"Apakah string `'{actual_string_to_transform}'` ada di daftar kelas encoder? **{is_known}**")
            print(f"Apakah string `'{actual_string_to_transform}'` ada di daftar kelas encoder? {is_known}")

            if is_known:
                transformed_array = encoder_object.transform(input_value_list) # Proses transform
                st.write(f"Hasil transform (array): `{transformed_array}`")
                print(f"Hasil transform (array): {transformed_array}")
                encoded_value_scalar = transformed_array[0]
            else:
                st.error(f"LABEL TIDAK DIKENAL untuk '{target_column_name}': String `'{actual_string_to_transform}'` tidak ditemukan di kelas encoder. Akan di-set ke NaN.")
                print(f"ERROR: LABEL TIDAK DIKENAL untuk '{target_column_name}': String `'{actual_string_to_transform}'` tidak ditemukan di kelas encoder. Akan di-set ke NaN.")
                encoded_value_scalar = np.nan

        st.write(f"Nilai yang akan dimasukkan ke df_processed['{target_column_name}']: `{encoded_value_scalar}`")
        print(f"Nilai yang akan dimasukkan ke df_processed['{target_column_name}']: {encoded_value_scalar}")
        df_processed[target_column_name] = encoded_value_scalar

    except Exception as e:
        st.error(f"EXCEPTION saat encoding '{target_column_name}': {e}")
        print(f"EXCEPTION saat encoding '{target_column_name}': {e}")
        df_processed[target_column_name] = np.nan # Pastikan NaN jika ada error lain
    # --- AKHIR DEBUGGING DETAIL UNTUK SATU KOLOM ---

    # Lanjutkan dengan encoding kolom kategorikal lainnya.
    # Anda bisa menerapkan blok try-except serupa atau pastikan inputnya selalu valid.
    # Contoh sederhana (tanpa debug detail untuk kolom lain, tapi tambahkan try-except):
    categorical_cols_to_encode = {
        "Course": encoder_Course,
        "Daytime_evening_attendance": encoder_Daytime_evening_attendance,
        "Debtor": encoder_Debtor,
        "Displaced": encoder_Displaced,
        "Educational_special_needs": encoder_Educational_special_needs,
        "Fathers_occupation": encoder_Fathers_occupation,
        "Fathers_qualification": encoder_Fathers_qualification,
        "Gender": encoder_Gender,
        "International": encoder_International,
        "Marital_status": encoder_Marital_status,
        "Mothers_occupation": encoder_Mothers_occupation,
        "Mothers_qualification": encoder_Mothers_qualification,
        "Nacionality": encoder_Nacionality,
        "Previous_qualification": encoder_Previous_qualification,
        "Scholarship_holder": encoder_Scholarship_holder,
        "Tuition_fees_up_to_date": encoder_Tuition_fees_up_to_date
    }

    for col_name, encoder in categorical_cols_to_encode.items():
        if col_name == "Application_mode": continue # Sudah di-debug di atas
        try:
            df_processed[col_name] = encoder.transform(data_copied[col_name])[0]
        except Exception as e_col:
            print(f"Error encoding '{col_name}': {e_col}. Mengisi dengan NaN.")
            st.warning(f"Error encoding '{col_name}'. Mengisi dengan NaN.") # Tampilkan warning di UI
            df_processed[col_name] = np.nan


    # Numerical Columns
    df_processed["Admission_grade"] = scaler_Admission_grade.transform(np.asarray(data_copied["Admission_grade"]).reshape(-1,1))[0]
    df_processed["Age_at_enrollment"] = scaler_Age_at_enrollment.transform(np.asarray(data_copied["Age_at_enrollment"]).reshape(-1,1))[0]
    df_processed["Application_order"] = scaler_Application_order.transform(np.asarray(data_copied["Application_order"]).reshape(-1,1))[0]
    df_processed["Curricular_units_1st_sem_without_evaluations"] = scaler_Curricular_units_1st_sem_without_evaluations.transform(np.asarray(data_copied["Curricular_units_1st_sem_without_evaluations"]).reshape(-1,1))[0]
    df_processed["Curricular_units_2nd_sem_without_evaluations"] = scaler_Curricular_units_2nd_sem_without_evaluations.transform(np.asarray(data_copied["Curricular_units_2nd_sem_without_evaluations"]).reshape(-1,1))[0]
    df_processed["GDP"] = scaler_GDP.transform(np.asarray(data_copied["GDP"]).reshape(-1,1))[0]
    df_processed["Inflation_rate"] = scaler_Inflation_rate.transform(np.asarray(data_copied["Inflation_rate"]).reshape(-1,1))[0]
    df_processed["Previous_qualification_grade"] = scaler_Previous_qualification_grade.transform(np.asarray(data_copied["Previous_qualification_grade"]).reshape(-1,1))[0]
    df_processed["Unemployment_rate"] = scaler_Unemployment_rate.transform(np.asarray(data_copied["Unemployment_rate"]).reshape(-1,1))[0]
    
    # PCA
    data_copied["Curricular_units_1st_sem_approved"] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data_copied["Curricular_units_1st_sem_approved"]).reshape(-1,1))[0]
    data_copied["Curricular_units_1st_sem_credited"] = scaler_Curricular_units_1st_sem_credited.transform(np.asarray(data_copied["Curricular_units_1st_sem_credited"]).reshape(-1,1))[0]
    data_copied["Curricular_units_1st_sem_enrolled"] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data_copied["Curricular_units_1st_sem_enrolled"]).reshape(-1,1))[0]
    data_copied["Curricular_units_1st_sem_evaluations"] = scaler_Curricular_units_1st_sem_evaluations.transform(np.asarray(data_copied["Curricular_units_1st_sem_evaluations"]).reshape(-1,1))[0]
    data_copied["Curricular_units_1st_sem_grade"] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data_copied["Curricular_units_1st_sem_grade"]).reshape(-1,1))[0]
    data_copied["Curricular_units_2nd_sem_approved"] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(data_copied["Curricular_units_2nd_sem_approved"]).reshape(-1,1))[0]
    data_copied["Curricular_units_2nd_sem_credited"] = scaler_Curricular_units_2nd_sem_credited.transform(np.asarray(data_copied["Curricular_units_2nd_sem_credited"]).reshape(-1,1))[0]
    data_copied["Curricular_units_2nd_sem_enrolled"] = scaler_Curricular_units_2nd_sem_enrolled.transform(np.asarray(data_copied["Curricular_units_2nd_sem_enrolled"]).reshape(-1,1))[0]
    data_copied["Curricular_units_2nd_sem_evaluations"] = scaler_Curricular_units_2nd_sem_evaluations.transform(np.asarray(data_copied["Curricular_units_2nd_sem_evaluations"]).reshape(-1,1))[0]
    data_copied["Curricular_units_2nd_sem_grade"] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data_copied["Curricular_units_2nd_sem_grade"]).reshape(-1,1))[0]
    df_processed[["pc1_1", "pc1_2", "pc1_3", "pc1_4", "pc1_5"]] = pca_1.transform(data_copied[pca_numerical_columns])
    


    st.write("--- Selesai data_preprocessing, mengembalikan df_processed ---")
    print("--- Selesai data_preprocessing, mengembalikan df_processed ---")
    # ... (print kolom dan nilai contoh df_processed seperti sebelumnya) ...
