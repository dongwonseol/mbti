import streamlit as st

# 질문 리스트
questions = [
    {"text": "학교 행사를 계획할 때, 당신은:", "options": [
        {"text": "세부 일정을 미리 꼼꼼히 짭니다.", "type": "J"},
        {"text": "큰 그림만 그리고 즉흥적으로 대처합니다.", "type": "P"}
    ]},
    {"text": "학생들과 대화할 때, 당신은:", "options": [
        {"text": "실제 경험과 구체적인 예시를 들어 설명합니다.", "type": "S"},
        {"text": "추상적인 개념과 이론을 활용해 설명합니다.", "type": "N"}
    ]},
    {"text": "동료 교사와의 갈등 상황에서, 당신은:", "options": [
        {"text": "논리적으로 문제를 분석하고 해결책을 찾습니다.", "type": "T"},
        {"text": "서로의 감정을 고려하며 조화로운 해결을 추구합니다.", "type": "F"}
    ]},
    {"text": "수업 후 휴식 시간에 당신은:", "options": [
        {"text": "다른 교사들과 대화하며 에너지를 얻습니다.", "type": "E"},
        {"text": "조용히 혼자만의 시간을 가지며 재충전합니다.", "type": "I"}
    ]},
    {"text": "새로운 교육 방법을 도입할 때, 당신은:", "options": [
        {"text": "기존의 검증된 방식을 선호합니다.", "type": "S"},
        {"text": "혁신적이고 창의적인 접근을 시도합니다.", "type": "N"}
    ]},
    {"text": "학생의 성적이 갑자기 떨어졌을 때, 당신은:", "options": [
        {"text": "객관적인 데이터를 분석하여 원인을 파악합니다.", "type": "T"},
        {"text": "학생과의 대화를 통해 감정적인 문제를 확인합니다.", "type": "F"}
    ]},
    {"text": "수업 준비를 할 때, 당신은:", "options": [
        {"text": "체계적으로 계획을 세우고 그대로 진행합니다.", "type": "J"},
        {"text": "대략적인 방향만 정하고 유연하게 대처합니다.", "type": "P"}
    ]},
    {"text": "교직원 회의에서 당신은:", "options": [
        {"text": "적극적으로 의견을 제시하고 토론에 참여합니다.", "type": "E"},
        {"text": "다른 사람들의 의견을 경청하고 신중히 생각합니다.", "type": "I"}
    ]},
    {"text": "학생들의 과제를 평가할 때, 당신은:", "options": [
        {"text": "정해진 기준에 따라 엄격하게 채점합니다.", "type": "T"},
        {"text": "학생의 노력과 진전을 고려하여 평가합니다.", "type": "F"}
    ]},
    {"text": "학교의 미래 계획을 논의할 때, 당신은:", "options": [
        {"text": "현실적이고 실현 가능한 목표에 집중합니다.", "type": "S"},
        {"text": "이상적이고 혁신적인 비전을 제시합니다.", "type": "N"}
    ]}
]

# MBTI 유형별 설명
personality_types = {
    "ISTJ": {"animal": "부엉이", "description": "체계적이고 책임감 있는 교육자"},
    "ISFJ": {"animal": "코알라", "description": "배려심 깊고 헌신적인 멘토"},
    "INFJ": {"animal": "돌고래", "description": "통찰력 있고 영감을 주는 가이드"},
    "INTJ": {"animal": "독수리", "description": "전략적이고 혁신적인 교육 설계자"},
    "ISTP": {"animal": "고양이", "description": "적응력 있고 문제 해결에 능한 실용주의자"},
    "ISFP": {"animal": "나비", "description": "창의적이고 유연한 예술 교육자"},
    "INFP": {"animal": "유니콘", "description": "이상주의적이고 학생 중심적인 교육자"},
    "INTP": {"animal": "올빼미", "description": "논리적이고 창의적인 교육 혁신가"},
    "ESTP": {"animal": "여우", "description": "활동적이고 실용적인 체험 학습 전문가"},
    "ESFP": {"animal": "오랑우탄", "description": "열정적이고 재미있는 학급 분위기 메이커"},
    "ENFP": {"animal": "돌고래", "description": "열정적이고 창의적인 동기부여자"},
    "ENTP": {"animal": "원숭이", "description": "혁신적이고 도전적인 아이디어 뱅크"},
    "ESTJ": {"animal": "사자", "description": "체계적이고 결단력 있는 학급 운영자"},
    "ESFJ": {"animal": "골든리트리버", "description": "사교적이고 협력적인 커뮤니티 빌더"},
    "ENFJ": {"animal": "펭귄", "description": "카리스마 있고 영감을 주는 리더"},
    "ENTJ": {"animal": "호랑이", "description": "비전있고 전략적인 교육 리더"}
}

# 사용자가 답한 내용 저장할 변수
answers = {}

# 현재 질문 인덱스
current_question = st.session_state.get('current_question', 0)

# 결과 표시 여부
result = st.session_state.get('result', None)

def calculate_result(answers):
    counts = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    for answer in answers.values():
        counts[answer] += 1

    # 결과 MBTI 타입 계산
    result = (
        ('E' if counts['E'] > counts['I'] else 'I') +
        ('S' if counts['S'] > counts['N'] else 'N') +
        ('T' if counts['T'] > counts['F'] else 'F') +
        ('J' if counts['J'] > counts['P'] else 'P')
    )
    return result

if result:
    st.header(f"당신의 교사 MBTI 유형은 {personality_types[result]['animal']}")
    st.subheader(personality_types[result]['description'])
    if st.button("다시 테스트하기"):
        st.session_state['current_question'] = 0
        st.session_state['result'] = None
else:
    # 현재 질문 가져오기
    question = questions[current_question]
    
    st.header(f"질문 {current_question + 1}")
    st.write(question["text"])
    
    for option in question["options"]:
        if st.button(option["text"]):
            answers[current_question] = option["type"]
            st.session_state['current_question'] = current_question + 1
            
            # 마지막 질문이면 결과 계산
            if current_question == len(questions) - 1:
                result_type = calculate_result(answers)
                st.session_state['result'] = result_type

# 진행 상황 표시
progress = (current_question + 1) / len(questions) * 100
st.progress(progress)
