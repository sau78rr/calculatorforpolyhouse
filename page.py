import streamlit as st

st.title('Polyhouse Input Page')

# Step 1: Show only polyhouse type selection first
polyhouse_type = st.selectbox('Select type of polyhouse:', ['', 'NVPH', 'NH', 'Fan and Pad'])

# Step 2: Show further options only if a valid type is selected
if polyhouse_type == 'NVPH':
    road = st.selectbox('Road:', ['Present', 'Absent'])
    bay_size = st.text_input('Bay size:')
    hockey_space = st.text_input('Hockey space:')
    type_of_structure = st.selectbox('Type of structure:', ['Stepper', 'Symmetric'])

    domes_list = None
    no_of_steps = None
    if type_of_structure == 'Stepper':
        no_of_steps = st.number_input('Number of steps:', min_value=1, step=1)
        domes_list = []
        for i in range(int(no_of_steps)):
            domes = st.number_input(f'Number of domes for step {i+1}:', min_value=0, step=1, key=f'domes_{i}')
            domes_list.append(domes)

    if st.button("Calculate"):
        # Example calculation: total domes if stepper, else 0
        if domes_list:
            total_domes = sum(domes_list)
            st.success(f"Total number of domes: {total_domes}")
        else:
            st.info("No domes to calculate.")

elif polyhouse_type in ['NH', 'Fan and Pad']:
    st.info(f"You selected '{polyhouse_type}'. No further inputs required for this type.")

else:
    st.info("Please select the type of polyhouse to proceed.")
