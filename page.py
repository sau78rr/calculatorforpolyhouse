import streamlit as st

st.title('Polyhouse Input Page')

# Step 1: Polyhouse type selection
polyhouse_type = st.selectbox('Select type of polyhouse:', ['', 'NVPH', 'Net House', 'Fan and Pad'])

if polyhouse_type == 'NVPH':
    road = st.selectbox('Road Inside:', ['', 'Present', 'Absent'])
    bay_size = st.text_input('Bay size:')
    hockey_space = st.text_input('Hockey space:')
    type_of_structure = st.selectbox('Type of structure:', ['', 'Stepper', 'Symmetric'])

    domes_list = []
    no_of_steps = None
    isstepper=False
    # Only show stepper fields if chosen
    if type_of_structure == 'Stepper':
        no_of_steps = st.number_input('Number of steps:', min_value=0, step=1, value=1)
        if(no_of_steps==0):
            domes=st.number_input(
                f'Enter the number of domes:',min_value=0,step=1,value=1
            )
            domes_list.append(domes)
        else:
            isstepper=True
            for i in range(int(no_of_steps)):
                domes = st.number_input(
                f'Number of domes for step {i+1}:',
                min_value=1,  # Set min_value=1 to require input
                step=1,
                key=f'domes_{i}'
            )
                domes_list.append(domes)

        
   

    # Calculate button and validation
    if st.button("Calculate"):
        missing_fields = []

        if road == '':
            missing_fields.append("Road")
        if not bay_size.strip():
            missing_fields.append("Bay size")
        if not hockey_space.strip():
            missing_fields.append("Hockey space")
        if type_of_structure == '':
            missing_fields.append("Type of structure")
        if type_of_structure == 'Stepper':
                if(isstepper):
                    if(no_of_steps==0):
                        missing_fields.append("Number of steps")
                for idx, domes in enumerate(domes_list):
                    if domes < 1:
                        missing_fields.append(f"Number of domes for step {idx+1}")

        if missing_fields:
            st.error("Please enter all required fields:\n- " + "\n- ".join(missing_fields))
        else:
            # Example calculation
            if type_of_structure == 'Stepper':
                total_domes = sum(domes_list)
                st.success(f"Total number of domes: {total_domes}")
            else:
                st.success("All fields are filled! (No calculation for symmetric structure in this example)")


elif polyhouse_type=='Net House':
    road = st.selectbox('Road Inside:', ['', 'Present', 'Absent'])
    bay_size = st.text_input('Bay size:')
    hockey_space = st.text_input('Hockey space:')
    type_of_structure = st.selectbox('Type of structure:', ['', 'Stepper', 'Symmetric'])

    domes_list = []
    no_of_steps = None

    # Only show stepper fields if chosen
    if type_of_structure == 'Stepper':
        no_of_steps = st.number_input('Number of steps:', min_value=0, step=1, value=1)
        if(no_of_steps==0):
            domes=st.number_input(
                f'Enter the number of domes:',min_value=0,step=1,value=1
            )
            domes_list.append(domes)
        else:
            for i in range(int(no_of_steps)):
                domes = st.number_input(
                f'Number of domes for step {i+1}:',
                min_value=1,  # Set min_value=1 to require input
                step=1,
                key=f'domes_{i}'
            )
                domes_list.append(domes)

        
   

    # Calculate button and validation
    if st.button("Calculate"):
        missing_fields = []

        if road == '':
            missing_fields.append("Road")
        if not bay_size.strip():
            missing_fields.append("Bay size")
        if not hockey_space.strip():
            missing_fields.append("Hockey space")
        if type_of_structure == '':
            missing_fields.append("Type of structure")
        if type_of_structure == 'Stepper':
            if not no_of_steps or no_of_steps < 1:
                missing_fields.append("Number of steps")
            for idx, domes in enumerate(domes_list):
                if domes < 1:
                    missing_fields.append(f"Number of domes for step {idx+1}")

        if missing_fields:
            st.error("Please enter all required fields:\n- " + "\n- ".join(missing_fields))
        else:
            # Example calculation
            if type_of_structure == 'Stepper':
                total_domes = sum(domes_list)
                st.success(f"Total number of domes: {total_domes}")
            else:
                st.success("All fields are filled! (No calculation for symmetric structure in this example)")


elif polyhouse_type in ['Net House', 'Fan and Pad']:
    st.info(f"You selected '{polyhouse_type}'. No further inputs required for this type.")

elif polyhouse_type == '':
    st.info("Please select the type of polyhouse to proceed.")
