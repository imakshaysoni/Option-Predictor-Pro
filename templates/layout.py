import streamlit as st


# Define the header
def streamlit_header():
    # Header
    st.markdown(
        """
        <style>
        .header {
            padding: 10px;
            background-color: #f0f0f0;
            display: flex;
            justify-content: center; /* Align items from start to end */
        }
        .icon {
            margin-right: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<div class="header">', unsafe_allow_html=True)

    # GitHub Icon with link
    st.markdown(
        '<a href="https://github.com/your-github-profile" target="_blank" class="icon"><img src="https://github.com/favicon.ico" width="30" height="30"></a>',
        unsafe_allow_html=True)

    # LinkedIn Icon with link
    st.markdown(
        '<a href="https://www.linkedin.com/in/your-linkedin-profile" target="_blank" class="icon"><img src="https://linkedin.com/favicon.ico" width="30" height="30"></a>',
        unsafe_allow_html=True)

    # LeetCode Icon with link
    st.markdown(
        '<a href="https://leetcode.com/your-leetcode-profile" target="_blank" class="icon"><img src="https://leetcode.com/favicon.ico" width="30" height="30"></a>',
        unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Main content of your application
    st.header("Welcome to my Streamlit application!", divider='grey')


# Define the footer
def streamlit_footer():
    # Footer
    st.text("If you like the project please rate it on github and share.")
    st.markdown(
        """
        <hr>
        <footer style="text-align: center; padding: 10px;">
            <p>&copy; 2024 Your Name. All rights reserved.</p>
            <p> Email Address: akshaysoni460@gmail.com </p>
            <a href="mailto:akshaysoni460@gmail.com">Contact me</a>
        </footer>
        """,
        unsafe_allow_html=True
    )

def streamlit_sidebar():
    # Sidebar
    # Sidebar
    st.sidebar.title('Connect with Me')

    # Website
    st.sidebar.markdown('**Website:**')
    st.sidebar.markdown(
        '<a href="https://akshaysoni.me" target="_blank" class="icon"><img src="https://akshaysoni.me/favicon.ico" width="30" height="30"></a>',
        unsafe_allow_html=True)


    # GitHub Icon with link
    st.sidebar.markdown('**GitHub:**')
    st.sidebar.markdown(
        '<a href="https://github.com/imakshaysoni" target="_blank" class="icon"><img src="https://github.com/favicon.ico" width="30" height="30"></a>',
        unsafe_allow_html=True)

    # LinkedIn Icon with link
    st.sidebar.markdown('**LinkedIn:**')
    st.sidebar.markdown(
        '<a href="https://www.linkedin.com/in/imakshaysoni" target="_blank" class="icon"><img src="https://linkedin.com/favicon.ico" width="30" height="30"></a>',
        unsafe_allow_html=True)

    # LeetCode Icon with link
    st.sidebar.markdown('**LeetCode:**')
    st.sidebar.markdown(
        '<a href="https://leetcode.com/iamakshaysoni" target="_blank" class="icon"><img src="https://leetcode.com/favicon.ico" width="30" height="30"></a>',
        unsafe_allow_html=True)
