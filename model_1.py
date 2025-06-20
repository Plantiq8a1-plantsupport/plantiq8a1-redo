import google.generativeai as genai

class PlantExpert:
    def __init__(self):
        self.ten = "chuyên gia tư vấn thuộc plantiq8a1"
        self.vai_tro = "Chuyên gia chăm sóc cây"
        self.luu_hoi_dap = []

        genai.configure(api_key="PLANTIQ8A1")
        self.model = genai.GenerativeModel(model_name="gemini-2.5-flash")

        self.prefix = (
            "Bạn là một chuyên gia chăm sóc cây có tên là 'chuyên gia tư vấn thuộc plantiq8a1'. "
            "Bạn chỉ tư vấn về cây, không tạo mã, không trả lời những chủ đề không liên quan. "
            "Bạn luôn dùng ngôn ngữ dễ hiểu cho học sinh và người mới trồng cây. "
            "Bạn luôn trả lời thân thiện, có emoji 🌱, và dựa vào câu hỏi trước nếu cần. "
            "Ví dụ: nếu tôi hỏi về vàng lá, bạn phải chẩn đoán và hướng dẫn chi tiết. "
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


# Plantiq8a1 
