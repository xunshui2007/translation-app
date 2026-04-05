"""
泰语翻译助手
Thai Translation Assistant

支持中文 ↔ 泰语互译
"""

import requests
import json
import re
from typing import Optional

class ThaiTranslator:
    """泰语翻译器"""
    
    def __init__(self, engine: str = "google"):
        """
        初始化翻译器
        
        Args:
            engine: 翻译引擎 ("google", "baidu", "youdao")
        """
        self.engine = engine
        self.google_url = "https://translate.googleapis.com/translate_a/single"
    
    def detect_language(self, text: str) -> str:
        """
        检测语言
        
        Args:
            text: 输入文本
            
        Returns:
            语言代码 ("zh" 中文, "th" 泰语)
        """
        # 泰语 Unicode 范围: 0E00-0E7F
        thai_pattern = re.compile(r'[\u0E00-\u0E7F]')
        if thai_pattern.search(text):
            return "th"
        
        # 中文 Unicode 范围
        chinese_pattern = re.compile(r'[\u4E00-\u9FFF]')
        if chinese_pattern.search(text):
            return "zh"
        
        return "auto"
    
    def translate_google(self, text: str, target_lang: str = "th") -> str:
        """
        使用 Google Translate 翻译
        
        Args:
            text: 要翻译的文本
            target_lang: 目标语言 ("th" 泰语, "zh" 中文)
            
        Returns:
            翻译结果
        """
        source_lang = "zh" if target_lang == "th" else "th"
        
        params = {
            "client": "gtx",
            "sl": source_lang,
            "tl": target_lang,
            "dt": "t",
            "q": text
        }
        
        try:
            response = requests.get(self.google_url, params=params, timeout=10)
            if response.status_code == 200:
                result = response.json()
                translated_text = "".join([item[0] for item in result[0] if item[0]])
                return translated_text
        except Exception as e:
            print(f"翻译错误: {e}")
        
        return text
    
    def translate(self, text: str, target_lang: Optional[str] = None) -> str:
        """
        翻译文本
        
        Args:
            text: 要翻译的文本
            target_lang: 目标语言 (可选，自动检测)
            
        Returns:
            翻译结果
        """
        if not target_lang:
            source_lang = self.detect_language(text)
            target_lang = "th" if source_lang == "zh" else "zh"
        
        if self.engine == "google":
            return self.translate_google(text, target_lang)
        
        return text


def main():
    """主函数 - 命令行交互"""
    translator = ThaiTranslator()
    
    print("=" * 50)
    print("泰语翻译助手 Thai Translation Assistant")
    print("=" * 50)
    print("输入 'quit' 退出")
    print("自动检测语言：中文 → 泰语，泰语 → 中文")
    print("-" * 50)
    
    while True:
        try:
            text = input("\n请输入要翻译的内容: ").strip()
            
            if text.lower() in ["quit", "exit", "q"]:
                print("再见！ลาก่อน!")
                break
            
            if not text:
                continue
            
            result = translator.translate(text)
            print(f"\n翻译结果: {result}")
            
        except KeyboardInterrupt:
            print("\n\n再见！ลาก่อน!")
            break
        except Exception as e:
            print(f"错误: {e}")


if __name__ == "__main__":
    main()
