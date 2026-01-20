import streamlit as st
from data import get_mo_price, get_mo_dividend
from model import classify_yield, expected_return, price_targets

st.set_page_config(
    page_title="MO Yield Regime Dashboard",
    layout="centered"
)

st.title("Altria (MO) Yield Regime Model")
st.caption("Empirical dividend-yield timing system")

st.divider()

if st.button("Run Model"):

    with st.spinner("Pulling live MO data..."):
        price = get_mo_price()
        dividend = get_mo_dividend()
        yield_now = dividend / price

        bucket = classify_yield(yield_now)
        exp_ret = expected_return(bucket)
        targets = price_targets(dividend)

    st.success("Model updated")

    col1, col2, col3 = st.columns(3)
    col1.metric("MO Price", f"${price:,.2f}")
    col2.metric("Annual Dividend", f"${dividend:.2f}")
    col3.metric("Current Yield", f"{yield_now*100:.2f}%")

    st.divider()

    st.subheader("Yield Regime Classification")
    st.write(f"**Current Regime Bucket:** {bucket}")
    st.write(f"**Empirical Forward 12M Return:** {exp_ret*100:.1f}%")

    st.divider()

    st.subheader("Buy-Zone Price Ladder")

    for k, v in targets.items():
        st.write(f"{k}: **${v:,.2f}**")

    st.divider()

    if bucket <= 1:
        st.warning("MO is expensive relative to its historical yield distribution.")
    elif bucket == 2:
        st.info("MO is fairly valued relative to its historical yield distribution.")
    else:
        st.success("MO is cheap relative to its historical yield distribution — historically strong forward returns.")

