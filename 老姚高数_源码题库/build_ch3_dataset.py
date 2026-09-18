"""
生成老姚高数第3章完整 116 题结构化数据 (以 3.x.y 标号) 并写入 js/laoyao_text_data.js
"""

import sys, os, json, re
sys.stdout.reconfigure(encoding='utf-8')

# We construct the 116 problems systematically for Chapter 3
ch3_data = {}

# Helper to add problem
def add_prob(sec_num, prob_num, sub_num, sec_title, kp, q, s):
    if sub_num:
        label = f"3.{sec_num}.{prob_num} ({sub_num})"
    else:
        label = f"3.{sec_num}.{prob_num}"
    ch3_data[label] = {
        "label": label,
        "sec": sec_title,
        "kp": kp,
        "question": q.strip(),
        "solution": s.strip()
    }

print("Generating Chapter 3 data...")
