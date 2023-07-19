import io
import streamlit as st

st.title("SIGNATURE")

st.markdown(
    """
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .word-spacing {
        line-height: 0.5em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#st.markdown('<p class = "word-spacing"><span>레몬드랍 * 6</span><span style = "margin : 10em;"></span><span>2.5</span></p>', unsafe_allow_html = True)
#st.markdown('<p class = "word-spacing"><span>가디언즈 오브 갤럭시</span><span style="margin: 9em;"></span><span>1.5</span></p>', unsafe_allow_html=True)
#st.markdown('<p class = "word-spacing"><span>데 킬러</span><span style="margin: 9em;"></span><span>1.6</span></p>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .left-corner {
        text-align: left;
        float: left;
    }
    .right-corner {
        text-align: right;
        float: right;
    }
    .clearfix::after {
        content: "";
        display: table;
        clear: both;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#st.markdown('<p class = "word-spacing"><div class="clearfix">', unsafe_allow_html=True)
st.markdown('<div class="left-corner">레몬드랍</div><div class="right-corner">2.5</div>', unsafe_allow_html=True)
#st.markdown('</div></p>', unsafe_allow_html=True)
st.markdown('<div class="left-corner">가디언즈 오브 갤럭시</div><div class="right-corner">1.5</div>', unsafe_allow_html=True)
#st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="left-corner">데 킬러</div><div class="right-corner">1.6</div>', unsafe_allow_html=True)
#st.markdown('</div>', unsafe_allow_html=True)
