import streamlit as st
from PIL import Image
def main():
    # Set page title and favicon
    st.set_page_config(page_title='My Portfolio', page_icon=':clipboard:')

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
        unsafe_allow_html=True
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
    st.write('Write about your personal projects and provide links to their GitHub repositories or live demos.')
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
    st.write('Embed links or previews of your Medium portfolio articles.')
    # YouTube video
    # st.write('### YouTube Video')
    # youtube_link = 'https://www.youtube.com/watch?v=N0lhoGcFbtU'
    # st.video(youtube_link)

    # Medium article
    st.write('### Medium Article')
    medium_link = 'https://medium.com/p/a3e4642fff09/edit'
    st.markdown(f"[Click here to read the article]({medium_link})")

def render_students():
    # Students section
    st.write('## Mentored Students')
    st.write('List the students you have mentored and their accomplishments.')

def render_experiences():
    # Students section
    st.write('## Past Experiences')
    st.write('List the students you have mentored and their accomplishments.')


if __name__ == '__main__':
    main()
