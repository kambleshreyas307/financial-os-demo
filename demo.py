import streamlit as st
import all_in_one

st.title("🚀 Financial OS Demo")

st.sidebar.header("Risk Threshold")
risk_threshold = st.sidebar.slider("Risk Threshold", 0.0, 1.0, 0.68)
st.sidebar.write(f"Using threshold: {risk_threshold:.2f}")

# Run the real model with this threshold
f1_score, gas_cost, losses_prevented = all_in_one.validate(risk_threshold=risk_threshold)

st.markdown("### Live validation from model:")
st.markdown(f"- **F1‑Score:** {f1_score:.1%} (Target: 95.2%)")
st.markdown(f"- **Gas Cost:** ${gas_cost:.6f} USDC/tx (Target: 0.0032)")
st.markdown(f"- **Losses Prevented:** ${losses_prevented:.1f}M (Target: 18.7M)")