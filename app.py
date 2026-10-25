# ════════════════════════════════════════════════════════════
#  المحاضرة ٢٣ · هيكل المشروع
#
#  هاد **هيكل جاهز** فيه كل اللي بنيناه بمحاضرات ٢٠–٢٢:
#      · تسجيل منظّم       (٢٢)
#      · عدّادات و /metrics (٢٢)
#      · فحص صحّة حقيقي    (٢٢)
#      · أكواد حالة صحيحة  (٢٠)
#
#  وشغلك إنت **بمكان واحد**:  دالة  جاوب()
#  دوّر على:   ⟵⟵⟵  شغلك هون  ⟶⟶⟶
#
#  التشغيل محلياً:  uvicorn app:app --reload
# ════════════════════════════════════════════════════════════
import os
import time
import logging

from fastapi import FastAPI, HTTPException, Request, Response

app = FastAPI(title="Psychology and Wellbeing Guide", version="1.0")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("project")

بدأت_الخدمة = time.time()
عدادات = {"requests_total": 0, "errors_total": 0,
          "latency_ms_sum": 0.0, "latency_ms_max": 0.0}
حسب_المسار = {}

API_KEY = os.environ.get("MODEL_API_KEY", "")


# ════════════════════════════════════════════════════════════
#  ⟵⟵⟵  شغلك هون  ⟶⟶⟶
#
#  ١ · عرّف معرفتك أو بياناتك
#  ٢ · واكتب دالة جاوب() — بتاخد سؤال وبترجّع (جواب, مصادر)
#
#  وبترجّع ("", []) لما ما تلاقي جواب — والخدمة بترجّع 404.
# ════════════════════════════════════════════════════════════

# مثال بسيط · بدّله بموضوع مشروعك
# المعرفة = {
#     "الدوام": ("الدوام من ٨ صباحاً لـ ٤ مساءً · الأحد للخميس.",
#                ["دليل الموظف · صفحة 3"]),
#     "الإجازة": ("رصيد الإجازة السنوية ١٤ يوم · وبتتقدّم قبلها بأسبوع.",
#                 ["دليل الموظف · صفحة 7"]),
#     "الراتب": ("الرواتب بتنزل آخر يوم عمل بالشهر.",
#                ["دليل الموظف · صفحة 2"]),
# }

المعرفة = {
    "علم النفس": (
        "علم النفس هو الدراسة العلمية للعقل والسلوك. يمكن أن تساعد المعرفة النفسية الناس على فهم التجارب ودعم الرفاهية، لكنها لا تشخّص حالتك.",
        ["APA Dictionary of Psychology"],
    ),
    "التوتر": (
        "قد يساعدك تمرين تأريض أو تنفّس هادئ على التعامل مع التوتر. اختر ما يناسبك، وتواصل مع مختص إذا كان التوتر يؤثر في حياتك.",
        ["WHO EMRO: Dealing with stress"],
    ),
    "التنفس": (
        "اجلس براحة وتنفس بلطف وبانتظام لبضع دقائق، من دون إجبار نفسك على نفس عميق. توقف إذا شعرت بدوار.",
        ["NHS: Breathing exercises for stress"],
    ),
    "التأريض": (
        "للتأريض، انتبه بهدوء لما تراه وتسمعه وتشعر به حولك. هذا تمرين عام للتركيز على اللحظة الحالية، وليس علاجاً بحد ذاته.",
        ["WHO EMRO: Dealing with stress"],
    ),
    "القلق": (
        "يشعر كثير من الناس بالقلق أحياناً. إذا كان يؤثر في يومك أو يصعب عليك التعامل معه، تحدّث مع شخص تثق به أو مختص صحي.",
        ["NHS: Anxiety, fear or panic"],
    ),
    "الأخصائي النفسي": (
        "يمكن للأخصائي النفسي المؤهل أن يساعدك على فهم ما تمر به ومناقشة خيارات الدعم المناسبة. اختر مختصاً مرخصاً في بلدك.",
        ["American Psychological Association"],
    ),
    "التشخيص": (
        "هذا التطبيق يقدم معلومات عامة ولا يستطيع تشخيص حالة نفسية. التشخيص يحتاج تقييماً من مختص صحي مؤهل.",
        ["American Psychological Association"],
    ),
    "خطر فوري": (
        "إذا كنت أنت أو شخص آخر في خطر فوري، اتصل بخدمات الطوارئ المحلية أو اذهب إلى أقرب قسم طوارئ. لا تنتظر رد هذا التطبيق.",
        ["خدمات الطوارئ المحلية"],
    ),
}


def جاوب(سؤال: str):
    """بتاخد سؤال · بترجّع (جواب, مصادر).

    ⟵ هاي الدالة اللي بتبدّلها بمشروعك.

    خيارات:
      · بحث بسيط بالكلمات — زي تحت
      · أو نادِ فريقك من محاضرة ١٧
      · أو نادِ n8n webhook تبعك
    """
    س = سؤال.strip()
    if not س:
        return "", []

    for مفتاح, (جواب, مصادر) in المعرفة.items():
        if مفتاح in س:
            return جواب, مصادر

    return "", []


# ─────────── ولو بدك تنادي فريقك من محاضرة ١٧ ───────────
#
# from my_team import فريقي
#
# def جاوب(سؤال: str):
#     نتيجة = فريقي.invoke({"question": سؤال})
#     return نتيجة.get("answer", ""), نتيجة.get("sources", [])
#
# ─────────── أو تنادي n8n ───────────
#
# import httpx
# N8N_URL = os.environ.get("N8N_WEBHOOK_URL", "")
#
# def جاوب(سؤال: str):
#     r = httpx.get(N8N_URL, params={"q": سؤال}, timeout=20)
#     if r.status_code != 200:
#         return "", []
#     d = r.json()
#     return d.get("answer", ""), d.get("sources", [])
#
# ════════════════════════════════════════════════════════════
#  ⟵⟵⟵  نهاية شغلك · تحت ما بتلمس إشي  ⟶⟶⟶
# ════════════════════════════════════════════════════════════


@app.middleware("http")
async def قيس_كل_طلب(request: Request, call_next):
    بلّش = time.perf_counter()
    رد = await call_next(request)
    مدة = (time.perf_counter() - بلّش) * 1000

    عدادات["requests_total"] += 1
    عدادات["latency_ms_sum"] += مدة
    if مدة > عدادات["latency_ms_max"]:
        عدادات["latency_ms_max"] = مدة
    if رد.status_code >= 400:
        عدادات["errors_total"] += 1

    مسار = request.url.path
    حسب_المسار[مسار] = حسب_المسار.get(مسار, 0) + 1

    مستوى = logging.WARNING if رد.status_code >= 400 else logging.INFO
    log.log(مستوى, "path=%s | status=%s | ms=%.1f",
            مسار, رد.status_code, مدة)
    return رد


@app.get("/")
def home():
    """صفحة الترحيب."""
    return {
        "service": app.title,
        "status": "running",
        "endpoints": ["/ask?q=سؤالك", "/health", "/metrics", "/docs"],
    }


@app.get("/ask")
def ask(q: str):
    """السؤال الرئيسي · وهاد اللي بيفحصه الفاحص."""
    جواب, مصادر = جاوب(q)
    # if not جواب:
    #     raise HTTPException(status_code=404,
    #                         detail=f"ما لقيت جواب لـ: {q}")

    if not جواب:
    raise HTTPException(
        status_code=404,
        detail={
            "message": f"ما لقيت جواب لـ: {q}",
            "suggestions": list(المعرفة.keys())[:5],
        },
    )
    return {"question": q, "answer": جواب, "sources": مصادر}


@app.get("/health")
def health(response: Response):
    """فحص صحّة بيفحص فعلاً."""
    فحوصات = {
        "knowledge_loaded": len(المعرفة) > 0,
        "can_answer": bool(جاوب(next(iter(المعرفة), ""))[0])
                      if المعرفة else False,
    }
    سليمة = all(فحوصات.values())
    if not سليمة:
        response.status_code = 503
    return {"status": "ok" if سليمة else "unhealthy",
            "checks": فحوصات,
            "key_loaded": bool(API_KEY)}


@app.get("/metrics")
def metrics():
    """أرقام خدمتك."""
    ن = عدادات["requests_total"]
    return {
        "uptime_seconds": round(time.time() - بدأت_الخدمة, 1),
        "requests_total": ن,
        "errors_total": عدادات["errors_total"],
        "latency_ms_avg": round(عدادات["latency_ms_sum"] / ن, 2) if ن else 0,
        "latency_ms_max": round(عدادات["latency_ms_max"], 2),
        "by_path": dict(حسب_المسار),
    }
