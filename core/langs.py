# core/langs.py

def get_texts(language="vi"):
    texts = {
        "vi": {
            "title": "🇻🇳 VN Vietnam AI Travel Planner",
            "description": "Lên kế hoạch chuyến đi hoàn hảo của bạn với AI ✨ Chỉ cần nhập mong muốn!",
            "input_placeholder": "✍️ Mô tả chuyến đi lý tưởng của bạn:",
            "generate_button": "⚡ Tạo lịch trình",
            "select_language": "🌐 Chọn ngôn ngữ giao diện:",
            "popular_destinations": "📍 Địa điểm nổi bật sẽ hiện ở đây.",
            "error_no_input": "⚠️ Vui lòng nhập nội dung mong muốn trước khi tạo lịch trình.",
            "loading": "🔄 Đang tạo lịch trình, vui lòng chờ..."
        },
        "en": {
            "title": "🇺🇸 US Vietnam AI Travel Planner",
            "description": "Plan your perfect trip to Vietnam with AI ✨ Just tell us what you want!",
            "input_placeholder": "✍️ Describe your ideal trip:",
            "generate_button": "⚡ Generate itinerary",
            "select_language": "🌐 Select interface language:",
            "popular_destinations": "📍 Highlighted destinations will appear here.",
            "error_no_input": "⚠️ Please enter your trip idea before generating.",
            "loading": "🔄 Generating itinerary, please wait..."
        }
    }

    return texts.get(language, texts["vi"])  # Fallback to Vietnamese
