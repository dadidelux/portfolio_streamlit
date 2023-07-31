import streamlit as st
from PIL import Image


def main():
    # Set page title and favicon
    st.set_page_config(page_title='My Portfolio', page_icon=':clipboard:')
    st.markdown(
        """
        <style>
         .css-1jc7ptx, 
         .e1ewe7hr3, 
         .viewerBadge_container__1QSob, 
         .styles_viewerBadge__1yB5_, 
         .viewerBadge_link__1S137, 
         .viewerBadge_text__1JaDK{ display: none; } 
         #MainMenu{ visibility: hidden; } 
         footer { visibility: hidden; } 
         header { visibility: hidden; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Render the header section
    render_header()

    # Render the about section
    render_about()

    # Render the projects section
    render_projects()

    # Render the articles section
    render_articles()

    # Render the students section
    render_students()

    render_experiences()

def render_header():
    # Custom CSS for styling
    st.markdown(
        """
        <style>
        .header {
            background-color: #f5f5f5;
            padding: 20px;
            text-align: center;
        }
        .header-image {
            display: block;
            margin: 0 auto;
            max-width: 300px;
            padding: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Header section
    img = Image.open("in.jpg")
    st.image(img)

def render_about():
    # About section
    st.write('## About')
    st.write('As an analytical educator with extensive experience in university settings, I am well-versed in the challenges of juggling research, administrative duties, and teaching responsibilities. As an expert in Data Science, my unwavering dedication to expanding our collective knowledge base drives me to undertake innovative and captivating research projects. My contributions have been recognized through multiple publications in reputable journals and invitations to speak at prominent conferences within my field')

def render_projects():
    # Projects section
    st.write('## Projects')
    st.write('Personal Project from Github.')
    medium_link = 'https://github.com/cite-sirbryan'
    streamlit_link = 'https://environmentor-enwqyrfplzxp5rhzzphbqt.streamlit.app/'
    st.markdown(f"[My Old Github ]({medium_link})")
    st.markdown(f"[Environmentor Environmentalist AI Chat Assistant and Chat Bot ]({streamlit_link})")
    
    st.write('## Dashboards')
    col1, col2, col3,col4,col5,col6,col7 = st.columns(7)

    # Display the first image in the first column
    with col1:
        img1 = Image.open('1.jpg')
        st.image(img1)

    # Display the second image in the second column
    with col2:
        img2 = Image.open('2.jpg')
        st.image(img2)

    # Display the second image in the second column
    with col3:
        img3 = Image.open('3.jpg')
        st.image(img3)
    # Display the second image in the second column
    with col4:
        img4 = Image.open('4.jpg')
        st.image(img4)
    # Display the second image in the second column
    with col5:
        img5 = Image.open('5.jpg')
        st.image(img5)
    # Display the second image in the second column
    with col6:
        img6 = Image.open('6.jpg')
        st.image(img6)
    # Display the second image in the second column
    with col7:
        img7 = Image.open('7.jpg')
        st.image(img7)

def render_articles():
    # Articles section
    st.write('## Articles')
    st.write('My Medium portfolio articles.')
    # YouTube video
    # st.write('### YouTube Video')
    # youtube_link = 'https://www.youtube.com/watch?v=N0lhoGcFbtU'
    # st.video(youtube_link)
    medium_link = 'https://medium.com/p/a3e4642fff09/edit'
    st.markdown(f"[Click here to read the article Practice Kmeans Clustering (Under Construction July)]({medium_link})")
    medium_link = 'https://medium.com/@dabryan.devopstechnologiesph/building-my-first-chatgpt-app-using-streamlit-and-gpt-4-7a324f4b2cf2'
    st.markdown(f"[Building my first ChatGPT app using Streamlit and GPT-4 (June-28-2023)]({medium_link})")
    medium_link = 'https://medium.com/@dabryan.devopstechnologiesph/a-review-on-the-google-data-analytics-professional-certificate-3963c8cf7bbc'
    st.markdown(f"[A review on the Google Data Analytics Professional Certificate (Jan-14-2023]({medium_link})")



def render_students():
    # Students section
    st.write('## Mentored Individuals')
    st.write('The List of my students whom I have worked with thier portfolio projects.')
    medium_link = 'https://medium.com/@mwjteves/428d8d77d3a9'
    st.markdown(f"[Integration of Python and Google Sheets in creating a cloud-based examination]({medium_link})")
    medium_link = 'https://medium.com/@qjvbbeldeniza/heat-load-calculator-6c87fa946034'
    st.markdown(f"[Python program for computing the size of Air-con to be used on household]({medium_link})")
    medium_link = 'https://medium.com/@engelgatus/python-project-bc508abaa53f'
    st.markdown(f"[Comparative Analysis of the Philippines Stock Exchange Index Data Against COVID-19 Announcement, Seasonality and Foreign Investors Using Python]({medium_link})")
    medium_link = 'https://medium.com/@mfngubaton/heart-failure-prediction-dataset-8847a87e88c9'
    st.markdown(f"[UNVEILING HEART FAILURE: EXPLORING KAGGLE’S DATASET FOR DETECTION ANALYSIS]({medium_link})")
    medium_link = 'https://medium.com/@msalosarito/exploring-the-titanic-dataset-analyzing-passengers-demographics-and-survival-rates-97f5ec953cdc'
    st.markdown(f"[Exploring the Titanic Dataset: Analyzing Passengers’ Demographics and Survival Rates]({medium_link})")
    medium_link = 'https://medium.com/@mfslmamoso/from-data-to-delight-unraveling-wine-quality-patterns-with-machine-learning-classifiers-94885ac92760'
    st.markdown(f"[From Data to Delight: Unraveling Wine Quality Patterns with Machine Learning Classifiers]({medium_link})")


def render_experiences():
    # Students section
    st.write('## Past Experiences')
    st.write('List past experiences.')
    col1, col2,col3,col4= st.columns(4)
    with col1:
        img_1 = Image.open('hearnshobbies_logo.jpg')
        st.image(img_1, width=100)
    with col2:
        st.write('Data Analyst/Data Ingestion \n2022 Present - Part- Time')
    

if __name__ == '__main__':
    main()
