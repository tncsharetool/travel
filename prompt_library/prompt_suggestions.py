from prompt_library.travel_prompts import prompts

def show_prompt_suggestions():
    try:
        st.markdown("💡 **Gợi ý để bạn thử:**")
        for item in prompts[:3]:
            st.markdown(f"- `{item}`")
    except Exception as e:
        st.info("Không thể tải gợi ý prompt.")

