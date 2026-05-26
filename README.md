# fraud-detection-dvc-pipeline

# Fraud Detection - Reproducible ML Pipeline with DVC

This repository contains a reproducible, end-to-end data preprocessing, splitting, and model training pipeline for a Fraud Detection machine learning project. The pipeline structure, data lineages, and dependencies are orchestrated dynamically using **DVC (Data Version Control)**.

## 🚀 Project Overview
The main objective of this project is to ensure that data preparation and model training steps are fully tracked, cached, and reproducible across different environments. If the raw data, the processing scripts, or the model hyperparameters change, DVC automatically detects which parts of the pipeline need to be re-run.

### Pipeline Architecture & Stages
The pipeline consists of three sequential stages defined in `dvc.yaml`:

1. **`process_data`**: 
   * **Inputs:** `data/raw/transactions.csv`, `src/data/process_data.py`
   * **Process:** Ingests raw transaction records, removes duplicates, handles missing (Null) values using Pandas.
   * **Output:** `data/processed/clean_transactions.csv`

2. **`split_data`**:
   * **Inputs:** `data/processed/clean_transactions.csv`, `src/data/split_data.py`
   * **Process:** Splits the clean dataset into training and testing sets.
   * **Outputs:** `data/processed/train.csv`, `data/processed/test.csv`

3. **`train`** *(New MLOps Update)*:
   * **Inputs:** `data/processed/train.csv`, `src/models/train.py`
   * **Parameters:** `params.yaml` -> Tracks `n_estimators` dynamically.
   * **Process:** Trains a `RandomForestClassifier` model using tracked hyperparameters.
   * **Output:** `models/model.pkl` (Binary artifact tracked via DVC).

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Data Manipulation & ML:** Pandas, Scikit-Learn
* **Data Lineage, Parameters & Pipelines:** DVC (Data Version Control)
* **Source Control:** Git

---

## ⚙️ Dynamic Parameter Configuration (`params.yaml`)
We decoupled model configurations from the codebase. You can easily tweak hyperparameters without editing the python scripts directly:

```yaml
# params.yaml
n_estimators: 200


n_estimatorsDVC'nin akıllı önbellekleme sistemi sayesinde, yalnızca içinde değişiklik yaparsanız params.yaml, çalıştırma işlemi ve aşamalarını dvc reproakıllıca atlayacak  ve yalnızca aşamayı yeniden çalıştıracaktır !process_datasplit_datatrain
💻 İşlem Hattı Nasıl Çalıştırılır?
Veri ve makine öğrenimi işlem hattının tamamını yerel olarak yeniden oluşturmak için şu adımları izleyin:

1. Depoyu Klonlayın
Bash
git clone [https://github.com/hasansivri/fraud-detection-dvc-pipeline.git](https://github.com/hasansivri/fraud-detection-dvc-pipeline.git)
cd fraud-detection-dvc-pipeline
2. Bağımlılıkları Yükleyin
Python, Pandas, Scikit-Learn ve DVC'nin kurulu olduğundan emin olun.

Bash
pip install pandas scikit-learn dvc
3. İşlem Hattını Yeniden Oluşturun (Reproduce)
Otomatik işlem hattı yürütmesini başlatmak veya parametre değişikliklerini uygulamak için şunu çalıştırın:

Bash
dvc repro
DVC, bağımlılıkları doğrulayacak, değişen veya etkilenen Python komut dosyalarını sırayla çalıştıracak (process_data.py -> split_data.py -> train.py) ve oluşturulan veri/model çıktılarını önbelleğe alacaktır.

4. İşlem Hattının Durumunu Kontrol Edin
Her şeyin güncel olduğundan ve hiçbir aşamanın eski olmadığından emin olmak için:

Bash
dvc status
📊 İşlem Hattı Bağımlılık Grafiği (DAG)
İşlem hattı başlatıldığında, DVC otomatik olarak Yönlendirilmiş Döngüsüz Grafik (DAG) oluşturur. Bunu terminalinizde şu komutla görselleştirebilirsiniz:

Bash
dvc dag
Beklenen Çıktı:

Düz metin
  +--------------+  
  | data/raw/... |  
  +--------------+  
          |         
          v         
    process_data    
          |         
          v         
     split_data     
          |         
          v         
        train
