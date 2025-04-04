# core/langs.py

def get_texts(language='vi'):
    texts = {
        "vi": {
            "title": "🇻🇳 VN Vietnam AI Travel Planner",
            "description": "Lên kế hoạch chuyến đi hoàn hảo của bạn với AI ✨ Chỉ cần nhập mong muốn!",
            "input_placeholder": "✍️ Mô tả chuyến đi lý tưởng của bạn:",
            "generate_button": "🚀 Tạo lịch trình",
            "select_language": "🌐 Chọn ngôn ngữ giao diện:"
        },
        "en": {
            "title": "🇺🇸 VN Vietnam AI Travel Planner",
            "description": "Plan your perfect trip to Vietnam with AI ✨ Just tell us what you want!",
            "input_placeholder": "✍️ Describe your ideal trip:",
            "generate_button": "🚀 Generate Itinerary",
            "select_language": "🌐 Select interface language:"
        }
    }
    return texts.get(language, texts["vi"])
