import google.generativeai as genai
from IoT import get_prompt  

class PlantExpert:
    def __init__(self):
        self.ten = "chuyên gia tư vấn thuộc plantiq8a1"
        self.vai_tro = "Chuyên gia chăm sóc cây"
        self.luu_hoi_dap = []

        genai.configure(api_key="API_KEY") # Get API here: https://aistudio.google.com/
        self.model = genai.GenerativeModel(model_name="GEMINI_MODEL") #Models: https://ai.google.dev/gemini-api/docs/models

        self.prefix = (
            "Bạn là một chuyên gia chăm sóc cây có tên là 'chuyên gia tư vấn thuộc plantiq8a1'. "
            "Bạn chỉ tư vấn về cây, không tạo mã, không trả lời những chủ đề không liên quan. "
            "Bạn luôn dùng ngôn ngữ dễ hiểu cho học sinh và người mới trồng cây. "
            "Bạn luôn trả lời thân thiện, có emoji 🌱, và dựa vào câu hỏi trước nếu cần. "
            "Ví dụ: nếu tôi hỏi về vàng lá, bạn phải chẩn đoán và hướng dẫn chi tiết. "
            + get_prompt()  
        )

    def traloicauhoi(self, cauhoi):
        self.luu_hoi_dap.append(cauhoi)

        if not self._cauhoi_lien_quan_cay(cauhoi):
            return "Tôi chỉ hỗ trợ các câu hỏi về cây trồng thôi nha 🌿. Bạn hỏi thử lại nhé! ❌"

        prompt = self.prefix + "\n\nCâu hỏi: " + cauhoi

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Đã xảy ra lỗi khi gọi Gemini 😢: {e}"

    def _cauhoi_lien_quan_cay(self, cauhoi):
        tu_khoa = ["cây", "trồng", "sâu bệnh", "vàng lá", "phân bón", "chăm sóc", "đất", "nước", "diệt cỏ"]
        cauhoi_lower = cauhoi.lower()
        return any(tu in cauhoi_lower for tu in tu_khoa)



