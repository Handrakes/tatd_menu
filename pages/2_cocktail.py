import io
import streamlit as st

st.markdown(
    """
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .left-corner {
        text-align: left;
        float: left;
        font-size : 1.3em;
        margin-top: 1em;
    }
    .right-corner {
        text-align: right;
        float: right;
        font-size : 1.3em;
        margin-top : 1em;
    }
    .space{
        font-size : 0.8em;
        margin-top : 0em;
        margin-bottom : 0.5em;
        line-height : 0em;
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

st.title('SIGNATURE')
st.markdown('<div class="left-corner">레몬드랍 * 6</div><div class="right-corner">2.5</div>', unsafe_allow_html=True)
st.markdown('<div class="space">달달하고 상큼한 원샷 칵테일 5%</div>', unsafe_allow_html=True)
st.image('images/manhattan.jpg')
#st.markdown('</div></p>', unsafe_allow_html=True)
st.markdown('<div class="left-corner">가디언즈 오브 갤럭시</div><div class="right-corner">1.5</div>', unsafe_allow_html=True)
st.markdown('<div class="space">피나콜라다 베이스의 밀키스 맛 칵테일 (2.4%)</div>', unsafe_allow_html=True)
st.image('images/guardians.jpg')
#st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="left-corner">데 킬러</div><div class="right-corner">1.6</div>', unsafe_allow_html=True)
st.markdown('<div class="space">데킬라 베이스의 생라임과 허브가 들어간 칵테일 13%</div>', unsafe_allow_html=True)
st.image('images/jungle-bird.jpg')
#st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="left-corner">PASSAT</div><div class="right-corner">1.5</div>', unsafe_allow_html=True)
st.markdown('<div class="space">패션 후르츠, 리치맛 칵테일 10%</div>', unsafe_allow_html=True)
st.image('images/passats.jpg')
