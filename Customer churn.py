
import pickle
import streamlit as st

#loading the trained model
pickle_in = open('Classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

@ st.cache_resource

# Defining the function which will make prediction using the data which the user input
def prediction(REGION, TENURE, MONTANT, FREQUENCE_RECH, REVENUE,
       ARPU_SEGMENT, FREQUENCE, DATA_VOLUME, ON_NET, ORANGE, TIGO,
       ZONE1, ZONE2, REGULARITY, TOP_PACK, FREQ_TOP_PACK):

    # Making Predictions
    prediction = classifier.predict([[REGION, TENURE, MONTANT, FREQUENCE_RECH, REVENUE,
       ARPU_SEGMENT, FREQUENCE, DATA_VOLUME, ON_NET, ORANGE, TIGO,
       ZONE1, ZONE2, REGULARITY, TOP_PACK, FREQ_TOP_PACK]])

    if prediction == 0:
        pred = "No Churn"
    else:
        pred = "Churn"

    return pred

# This is the main function in which we define our webpage
def main():
    # Front end elements of the web page
    html_temp = '''
    <div style="background-color: #F4D03F; padding:10px">
    <h2 style="color: black; text-align: center;">Customer Churn Prediction App</h2>
    </div>
    '''
    # Display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # Following lines create boxes in which the user can enter data required to make prediction
    REGION = st.number_input("Region")
    REVENUE = st.number_input("Revenue")
    TENURE = st.number_input("Tenure (in months)")
    FREQUENCY = st.slider("Frequency", 1, 200)
    DATA_VOLUME = st.number_input("Data Volume")
    FREQUENCE_RECH = st.number_input("Frequency of Recharge")
    ARPU_SEGMENT = st.number_input("ARPU Segment")
    MONTANT = st.number_input("MONTANT")
    ON_NET = st.number_input("On Net")
    ORANGE = st.number_input("Orange")
    TIGO = st.number_input("Tigo")
    ZONE1 = st.number_input("Zone 1")
    ZONE2 = st.number_input("Zone 2")
    REGULARITY = st.number_input("Regularity")
    TOP_PACK = st.number_input("Top Pack")
    FREQ_TOP_PACK = st.number_input("Frequency of Top Pack")
    

    result = ""

    # When 'Predict' is clicked, make prediction and store it
    if st.button("Predict"):

        result = prediction(REGION, REVENUE, TENURE, FREQUENCY, DATA_VOLUME, FREQUENCE_RECH, ARPU_SEGMENT, MONTANT, ON_NET, ORANGE, TIGO, ZONE1, ZONE2, REGULARITY, TOP_PACK, FREQ_TOP_PACK)
        st.success("Prediction: {}".format(result))

if __name__ == '__main__':
    main()
