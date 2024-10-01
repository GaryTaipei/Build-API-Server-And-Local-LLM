# Build-API-Server-And-Local-LLM
這個專案是以 FastAPI 建置 API Server 定義 api 來詢問地端語言模型，地端語言模型為 Ollama 3.1 8b  

1.下載及安裝 Ollama 網址: https://ollama.com/  

2.安裝完成後將 model pull 到本機，在command 視窗中下指令: ollama pull llama 3.1:8b 或是 ollama pull mistral  

3.檢視本機目前下載的 model，在command 視窗中指令: ollama list  

4.執行 model 指令: ollama run llama 3.1:latest 或是 ollama run mistral  

5.model 跑起來後就可以試著在視窗中打字詢問問題，model 有回覆就表示成功在本機執行 ollama 了  

6.找一個資料夾作為專案程式的存放資料夾例如筆電C:槽下建立 "python_repos" 資料夾  

7.在command 視窗下指令 C:\python_repos> git clone https://github.com/GaryTaipei/Build-API-Server-And-Local-LLM.git  

8.會將 Repository 專案程式複製到本機 C:\python_repos\Build-API-Server-And-Local-LLM 資料夾  

9.建立 python 虛擬環境: python -m venv Build-API-Server-And-Local-LLM  

10. 打開 VS Code 開啟 Build-API-Server-And-Local-LLM 資料夾，然後將編譯器指向虛擬環境 檢視>命令選擇區 >Python 選取解義器 > 輸入解義器路徑 > 尋找 > 然後從檔案瀏覽視窗找到 Build-API-Server-And-Local-LLM 資料夾下的 Scripts 資料夾，選擇 python.exe  

11.安裝所需的套件: 在 VS Code 終端機輸入: pip install -r requirements.txt  

12.等待套件安裝完成後在終端機輸入: python .\main.py ，程式會以 FastAPI 運行一個 API Server(http://0.0.0.0:8000) ，可以試著以 CURL 指令或是 Postman 對著 API Server 下Post 查詢(http://localhost:8000/chat) 加上 header 參數 "Content-Type": "application/json"， body 內容:   
{
    "model" : "mistral",
    "prompt" : "How to get to Taipei 101 building?"
}  
