import streamlit as st

def input_page():
    st.title('Polyhouse Input Page')

    polyhouse_type = st.selectbox('Select type of polyhouse:', ['NVPH', 'NH', 'Fan and Pad'])

    if polyhouse_type == 'NVPH':
        road = st.selectbox('Road:', ['Present', 'Absent'])
        bay_size = st.text_input('Bay size:')
        hockey_space = st.text_input('Hockey space:')
        type_of_structure = st.selectbox('Type of structure:', ['Stepper', 'Symmetric'])

        if type_of_structure == 'Stepper':
            no_of_steps = st.number_input('Number of steps:', min_value=1, step=1)
            domes_list = []
            for i in range(no_of_steps):
                domes = st.number_input(f'Number of domes for step {i+1}:', min_value=0, step=1)
                domes_list.append(domes)
        else:
            no_of_steps = None
            domes_list = None

        return polyhouse_type, road, bay_size, hockey_space, type_of_structure, no_of_steps, domes_list
    else:
        return polyhouse_type, None, None, None, None, None, None

# To use this, call input_page() in your Streamlit app.
