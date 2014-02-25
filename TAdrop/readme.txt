作業三 文件分類

「文件分類」（document classification or text categorization）是指依文件「內容主旨」給定「類別」（class or category）的意思。例如，新聞文件可按其報導的內容，給予「政治」、「外交」、「娛樂」、「運動」等
類別。通常，這些類別都是事先定義或選定，以符合管理者的需求與期望。而給定類別的工作，傳統上都由人工閱覽文件，根據其主題大意，給予適當的類別標示。文件分類是圖書館學中資訊組織與主題分析領域裡一項非常重要的課題，也是現今知識管理主要的應用工具之一。

簡述作業內容如下：

1. 以20 Newsgroups的文件為基礎，擷取該資料集中的類別：comp.graphics與comp.windows.x，各取500篇文章。
2. 隨機取出400篇與comp.graphics相關的文章以及400篇與comp.windows.x相關的文章作為Training data (提供所屬label data與word對照表)，剩餘的200篇文章作為testing data(不提供label data)。

3. 請同學以2-4人為一組(成員自行決定)，互相討論，於3/5前將程式碼與Training data的分類結果(output格式為：Confusion matrix)，以及testing data的預測結果(格式請參考training data的label data)。上傳至E3平台。並於：

4. 3/6上課前繳交紙本，內容包含：Training data分類結果與testing data的預測結果。

請注意，不可以使用matlab或python內含之工具箱或演算法函式，請用自己的邏輯架構來完成程式碼撰寫

文件內容說明：提供training data(train.txt)與對應的label(train_label.txt)、testing data(test.txt)以及詞彙對照表(word.txt)

1) training set 包含：
	- train.txt       (dataMatrix, 800 x 228  - 800 vectors with dimensionality 228) 
	- train_label.txt (outcomeMatrix, 800 x 1 - 800 vectors with one dimension)
2) testing set 包含：
	- test.txt        (dataMatrix, 200 x 228  - 200 vectors with dimensionality 228)
	
3) word.txt (Vocabulary file)
	

例如：
train.txt: 　　       train_label.txt:
1 3 5 12	<====>    1
2 4 6 7	              2

word.txt:
lord
of
the
rings

從這三個檔案可表示為
第一篇文章：lord出現1次，of出現3次，the出現5次，rings出現12次，屬於第一類
第二篇文章：lord出現2次，of出現4次，the出現6次，rings出現7次，屬於第二類

請利用training data及對應的label求出training data的Confusion matrix與testing data的預測label為何?
