%matplotlib inline
# عرض الرسومات مباشرة أسفل خلية الكود في برنامج Jupyter Notebook.

import pandas as pd
# استيراد مكتبة بانداز (Pandas) للتعامل مع البيانات وتنظيمها في جداول.

import numpy as np
# استيراد مكتبة نامباي (NumPy) لإجراء العمليات الحسابية والتعامل مع المصفوفات الرقمية.

import matplotlib.pyplot as plt
# استيراد أدوات ماتبلوتليب (Matplotlib) لإنشاء الرسومات البيانية وتعديل شكلها.

import seaborn as sns
# استيراد مكتبة سيبورن (Seaborn) لإنشاء رسومات إحصائية واضحة ومنظمة.

from sklearn.preprocessing import LabelEncoder, StandardScaler
# استيراد أداة (LabelEncoder) لتحويل الفئات النصية إلى أرقام.
# واستيراد أداة (StandardScaler) لتوحيد مقاييس الأعمدة الرقمية.

from sklearn.feature_selection import SelectKBest, f_classif
# استيراد أداة (SelectKBest) لاختيار عدد محدد من الخصائص المهمة.
# واستيراد (f_classif) لتقييم الخصائص حسب اختلاف قيمها بين فئات الهدف.

sns.set_style("whitegrid")
# ضبط نمط الرسومات بخلفية بيضاء وخطوط شبكة لتسهيل قراءة البيانات.

plt.rcParams["figure.figsize"] = (10, 5)
# تحديد حجم الرسومات الافتراضي، بحيث يكون العرض 10 بوصات والارتفاع 5 بوصات.

pd.set_option("display.width", 100)
# تحديد عرض عرض الجداول النصية لتقليل تداخل الأعمدة عند إظهار البيانات.

pd.set_option("display.max_columns", 20)
# تحديد الحد الأقصى للأعمدة التي تظهر عند عرض الجداول وهو 20 عمودًا.

print("All packages loaded successfully.")
# طباعة رسالة تؤكد أن أسطر الاستيراد والإعداد السابقة نُفذت دون أخطاء.