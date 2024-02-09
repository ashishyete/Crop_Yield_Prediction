import streamlit as st
from gtts import gTTS
from io import BytesIO





st.title('Crop Yield Prediction :seedling:')

st.write(
    '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In the rapidly changing global landscape, accurate prediction '
    'of crop yield is vital for effective agricultural strategies and food security. Crop yield, the ratio of '
    'input to output in agriculture, serves as a key indicator of productivity influenced by factors like'
    'production measures, pests, environment, and consumer demand. Monitoring crop yield is crucial for informed'
    'decision-making, guiding policies, import/export considerations, pricing, and future crop '
    'planning. Various methods, including vegetation indices and statistical models, are employed by researchers for precise '
    'crop yield prediction.')
st.markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Crop yield prediction, a crucial aspect of agriculture, '
         'helps estimate the potential '
         'production of a specific crop in a particular location. Accurate crop yield forecasts benefit farmers, '
         'agribusinesses, and governmental agencies in making informed decisions related to crop planting, harvesting,'
         'and marketing. Accurate crop yield predictions empower farmers to optimize resource management, aiding in '
         'crop selection, fertilizer dosage, and ideal planting/harvesting timing. Improved planning involves '
         'anticipating harvest needs for marketing, storage, and transportation. These predictions enhance '
         'decision-making for agribusinesses and governments, influencing crop purchase, sale, and import decisions,'
         ' promoting food security. Additionally, precise forecasts contribute to increased food security by preventing'
         ' shortages, price fluctuations, and waste. They also support sustainable agriculture by minimizing resource '
         'wastage, facilitated by advanced data processing using machine learning techniques on historical and '
         'environmental data in the crop yield forecast model. **This application aims to assist users in predicting crop yield for effective agricultural strategies and food security.**')

if st.button("Generate Speech"):
    sound_file = BytesIO()
    tts = gTTS(
        'Crop Yield Prediction. In the rapidly changing global landscape, accurate prediction of crop yield is vital for effective agricultural strategies and food security. Crop yield, the ratio of input to output in agriculture, serves as a key indicator of productivity influenced by factors likeproduction measures, pests, environment, and consumer demand. Monitoring crop yield is crucial for informeddecision-making, guiding policies, import/export considerations, pricing, and future crop planning. Various methods, including vegetation indices and statistical models, are employed by researchers for precise crop yield prediction.'

        'Crop yield prediction, a crucial aspect of agriculture, helps estimate the potential production of a specific crop in a particular location. Accurate crop yield forecasts benefit farmers, agribusinesses, and governmental agencies in making informed decisions related to crop planting, harvesting,and marketing. Accurate crop yield predictions empower farmers to optimize resource management, aiding in crop selection, fertilizer dosage, and ideal planting/harvesting timing. Improved planning involves anticipating harvest needs for marketing, storage, and transportation. These predictions enhance decision-making for agribusinesses and governments, influencing crop purchase, sale, and import decisions, promoting food security. Additionally, precise forecasts contribute to increased food security by preventing shortages, price fluctuations, and waste. They also support sustainable agriculture by minimizing resource wastage, facilitated by advanced data processing using machine learning techniques on historical and environmental data in the crop yield forecast model. This application aims to assist users in predicting crop yield for effective agricultural strategies and food security.',
        lang='en')
    tts.write_to_fp(sound_file)

    st.audio(sound_file)

col1, col2, col2, col4, col5 = st.columns(5)

with col1:

    st.page_link("1_🏠_HomePage.py", label="Previous", icon="⬅")

with col5:

    st.page_link("pages/3_📚_Dataset.py", label="Next", icon="➡")