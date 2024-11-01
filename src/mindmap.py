import networkx
import pyvis

SAVE_NAME = "out/mindmap.html"

nx_G = networkx.Graph()

pairs = [
    ("COIN", "自然言語処理(NLP)"),
    ("自然言語処理(NLP)", "固有表現抽出(NER)"),
    ("自然言語処理(NLP)", "固有表現抽出(NER)"),
    ("固有表現抽出(NER)", "ラベル付きコーパス"),
    ("固有表現抽出(NER)", "情報抽出"),
    ("固有表現抽出(NER)", "医療"),
    ("ラベル付きコーパス", "補助コーパス"),
    ("ラベル付きコーパス", "コーパス"),
    ("自然言語処理(NLP)", "シーングラフ"),
    ("シーングラフ", "相互情報量"),
    ("自然言語処理(NLP)", "オントロジー構築"),
    ("オントロジー構築", "トリプル作成"),
    ("トリプル作成", "イベント"),
    ("トリプル作成", "主語・述語・目的語"),
    ("トリプル作成", "交通"),
    ("エンティティ抽出(ER)", "エンティティリンキング(EL)"),
    ("固有表現抽出(NER)", "エンティティリンキング(EL)"),
    ("自然言語処理(NLP)", "言語モデル(LM)"),
    ("言語モデル(LM)", "大規模言語モデル(LLM)"),
    ("大規模言語モデル(LLM)", "ファインチューニング"),
    ("ファインチューニング", "LowRankAdaption(LoRA)"),
    ("LowRankAdaption(LoRA)", "医療"),
    ("LowRankAdaption(LoRA)", "生物"),
    ("言語モデル(LM)", "BERT"),
    ("BERT", "Transformer"),
    ("大規模言語モデル(LLM)", "GPT"),
    ("GPT", "Transformer"),
    ("Transformer", "Attention"),
    ("大規模言語モデル(LLM)", "Llama"),
    ("自然言語処理(NLP)", "分類"),
    ("分類", "感情分類"),
    ("分類", "ZeroShotLearning"),
    ("自然言語処理(NLP)", "手話"),
    ("手話", "深層学習(DL)"),
    ("深層学習(DL)", "コンピュータビジョン(CV)"),
    ("自然言語処理(NLP)", "質問応答"),
    ("質問応答", "BERT"),
    ("質問応答", "系列変換モデル"),
    ("質問応答", "弱教師あり学習"),
    ("質問応答", "情報検索"),
    ("情報検索", "TF-IDF"),
    ("情報検索", "BM25"),
    ("TF-IDF", "固有表現抽出(NER)"),
    ("自然言語処理(NLP)", "知識グラフ(KG)"),
    ("知識グラフ(KG)", "知識グラフ埋め込み(KGE)"),
    ("知識グラフ埋め込み(KGE)", "二項関係"),
    ("二項関係", "トリプル作成"),
    ("知識グラフ埋め込み(KGE)", "TransE"),
    ("TransE", "TransR"),
    ("TransE", "RotatE"),
    ("知識グラフ(KG)", "マテリアルズインフォマティクス"),
    ("知識グラフ(KG)", "文献グラフ"),
    ("文献グラフ", "リンク予測"),
    ("知識グラフ(KG)", "深層確率モデル"),
    ("深層確率モデル", "薬物データベース"),
    ("知識グラフ(KG)", "グラフニューラルネットワーク(GNN)"),
    ("知識グラフ(KG)", "近傍知識グラフ"),
    ("自然言語処理(NLP)", "文誤り検知"),
    ("文誤り検知", "変分オートエンコーダ(VAE)"),
    ("文誤り検知", "敵対的オートエンコーダ(AAN)"),
    ("自然言語処理(NLP)", "関係抽出(RE)"),
    ("関係抽出(RE)", "情報抽出"),
    ("関係抽出(RE)", "機械加工文書"),
    ("COIN", "時系列データ"),
    ("時系列データ", "人工データ拡張"),
    ("時系列データ", "Informer"),
    ("時系列データ", "NeuralLaplace"),
]

nx_G.add_edges_from(pairs)

pyvis_G = pyvis.network.Network(height="1080px")
pyvis_G.from_nx(nx_G)
for node in pyvis_G.nodes:
    node["shape"] = "box"
pyvis_G.save_graph(SAVE_NAME)
