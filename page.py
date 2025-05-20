import streamlit as st

st.title('Polyhouse Input Page')

# Show only polyhouse type selection first
polyhouse_type = st.selectbox('Select type of polyhouse:', ['', 'NVPH', 'NH', 'Fan and Pad'])

if polyhouse_type == 'NVPH':
    road = st.selectbox('Road:', ['', 'Present', 'Absent'])
    bay_size = st.text_input('Bay size:')
    hockey_space = st.text_input('Hockey space:')
    type_of_structure = st.selectbox('Type of structure:', ['', 'Stepper', 'Symmetric'])

    domes_list = None
    no_of_steps = None
    all_inputs_filled = True
    missing_fields = []

    if type_of_structure == 'Stepper':
        no_of_steps = st.number_input('Number of steps:', min_value=1, step=1)
        domes_list = []
        for i in range(int(no_of_steps)):
            domes = st.number_input(f'Number of domes for step {i+1}:', min_value=0, step=1, key=f'domes_{i}')
            domes_list.append(domes)
            if domes == 0:
                missing_fields.append(f"Number of domes for step {i+1}")
                all_inputs_filled = False

    # Validation for empty fields
    if st.button("Calculate"):
        if road == '':
            missing_fields.append("Road")
            all_inputs_filled = False
        if not bay_size:
            missing_fields.append("Bay size")
            all_inputs_filled = False
        if not hockey_space:
            missing_fields.append("Hockey space")
            all_inputs_filled = False
        if type_of_structure == '':
            missing_fields.append("Type of structure")
            all_inputs_filled = False
        if type_of_structure == 'Stepper' and (no_of_steps is None or no_of_steps < 1):
            missing_fields.append("Number of steps")
            all_inputs_filled = False

        if all_inputs_filled:
            if domes_list:
                total_domes = sum(domes_list)
                st.success(f"Total number of domes: {total_domes}")
            else:
                st.info("No domes to calculate.")
        else:
            missing_str = ", ".join(missing_fields)
            st.error(f"Please enter all required fields. Missing: {missing_str}")

elif polyhouse_type in ['NH', 'Fan and Pad']:
    st.info(f"You selected '{polyhouse_type}'. No further inputs required for this type.")

else:
    st.info("Please select the type of polyhouse to proceed.")
