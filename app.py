import streamlit as st

st.markdown(
        f"""
<style>
    .appview-container .main .block-container{{
        max-width: 1050px;
        padding-top: 50px;
        padding-right: 200px;
        padding-left: 10px;
        padding-bottom: 10px;
    }}
    iframe{{
     width: 800px;
     margin:auto;
     display:block;
    }}
</style>
""",
        unsafe_allow_html=True,
    )

def main():
    st.title('Morris-Thorne Wormhole Visualization')
    latex_content = r"""
    \text{There are absolutely more refined and educated techniques to be used when assessing this concept, but I'll give you a relatively simple path to start down.}\\
    \text{The Morris-Thorne metric is a way of representing a simple, non-rotating wormhole:}\\
    ds^{2} = -\exp(2\Phi(r)) dt^{2} + \frac{dr^{2}}{1 - \frac{b(r)}{r}} + r^{2} (d\theta^{2} + \sin^{2} \theta d\phi^{2})\\
    \text{where } \Phi(r) \text{ is the redshift function and } b(r) \text{ is the shape function. For a traversable wormhole, } b(r) \text{ must satisfy the flare-out condition at the throat. The throat is defined at the minimum radius } r_{0} \text{ where the wormhole is the narrowest. The conditions are}\\
    \text{At the throat } r = r_{0}, \text{ the shape function satisfies: } b(r_{0}) = r_{0}\\
    \text{The derivative of the shape function } b'(r) \text{ must satisfy } b'(r_{0}) < 1 \text{ at the throat. This is necessary to ensure that the throat is a minimum radius and that the wormhole opens up (flares out) on either side of the throat.}\\
    \text{To ensure the wormhole is traversable, } \Phi(r) \text{ must be finite everywhere, i.e.,} \exp(2\Phi(r)) \neq 0 \ \forall r \text{ which means there are no horizons (regions from which light cannot escape)}\\
    \text{For this metric, the components of the stress-energy tensor } T_{\mu\nu} \text{ can be calculated using the Einstein field equations. They will depend on the form of } b(r) \text{ but you will find that they involve terms that represent negative energy density. This is a clear violation of the Null Energy Condition } T_{\mu\nu} k^{\mu} k^{\nu} \geq 0 \text{ which implies that the energy density measured by an observer moving along a null trajectory is non-negative.}\\
    \text{This is why you often hear that exotic matter is needed to keep a wormhole open and "operating".}\\
    \text{Anyways, from here you must do some non-trivial extensions. For one, the metric needs to be time-dependent. The shape and redshift functions now behave as } b(r,t) \text{ and } \Phi(r,t). \text{ I recommend perturbing the original shape function } b_{0}(r) \text{ with a small, time-dependent perturbation so that } b(r,t) = b_{0}(r) + f(t). \text{ The choice of } f(t) \text{ can model the motion characteristics (i.e., a sinusoidal } f(t) \text{ could represent an oscillating wormhole throat.}\\
    \text{We also need to define wormhole motion. Maybe start by translating the entire wormhole metric through a background spacetime or even a dynamic spacetime fabric where the wormhole itself changes its position.}\\
    \text{Next, you need to manage the interaction of the wormholes. A framework that describes both simultaneously is advantageous. You might superimpose two wormhole metrics - however, this is highly non-trivial using Einstein's equations. You must investigate the stability and singularities as two wormholes come in close proximity.}
    """

    st.latex(latex_content)


    # Define your sliders for the parameters of the shape and redshift functions
    # Example:
    r0 = st.sidebar.slider('Throat radius r0', 0.1, 2.0, 1.0)

    # More parameters and sliders...

    # Calculate wormhole properties based on the parameters
    # Example:
    # b_r = calculate_shape_function(r, r0, ...)
    # phi_r = calculate_redshift_function(r, ...)

    # Visualize the wormhole
    # fig = visualize_wormhole(b_r, phi_r, ...)
    # st.pyplot(fig)

if __name__ == "__main__":
    main()