# 泰语翻译助手

一个简单的泰语翻译程序，支持中文 ↔ 泰语互译。

## 功能

- 中文翻译为泰语
- 泰语翻译为中文
- 支持批量翻译
- 自动检测语言

## 安装

```bash
pip install -r requirements.txt
```

## 使用

```python
from translator import ThaiTranslator

translator = ThaiTranslator()

# 中文翻译泰语
result = translator.translate("你好", target_lang="th")
print(result)  # สวัสดี

# 泰语翻译中文
result = translator.translate("สวัสดี", target_lang="zh")
print(result)  # 你好
```

## API 说明

支持以下翻译引擎：

1. **Google Translate API** (免费，需要翻墙)
2. **百度翻译 API** (需要申请 API Key)
3. **有道翻译 API** (需要申请 API Key)

## 常用泰语词汇

| 中文 | 泰语 | 发音 |
|------|------|------|
| 你好 | สวัสดี | sawatdee |
| 谢谢 | ขอบคุณ | khob khun |
| 再见 | ลาก่อน | laa gon |
| 是 | ใช่ | chai |
| 不是 | ไม่ใช่ | mai chai |
| 对不起 | ขอโทษ | kho thot |
| 没关系 | ไม่เป็นไร | mai pen rai |
| 多少钱 | เท่าไร | tao rai |

## License

MIT
