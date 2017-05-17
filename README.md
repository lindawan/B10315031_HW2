#B10315031_HW2
BMP圖片使用DES加解密  

##建置環境
**OS:** &nbsp;macOS 10.12.4   
**Programming Language:** &nbsp;Python 2.7.13

##完成功能
1.  加解密模式：  
    *   ECB
    *   CBC
    *   OFB
    *   CTR

2.  圖片處理：
    *   RGB separately
    *   RGB continuously

3.  各種模式執行時間

##執行結果
**執行指令：**   
```python testDesBmp.py```  

**執行結果：**  
![result](https://github.com/lindawan/B10315031_HW2/blob/master/result.png)

沒有最佳化加解密時間，執行速度很慢 

##附加說明
*   **des.py**: &nbsp;DES加解密方法
  
*   **testDesBmp.py**:  &nbsp;測試BMP圖檔使用DES

*   **test.bmp**:&nbsp;原始圖檔

*   輸出圖檔檔名命名方式：   
    **mode**:&nbsp;&nbsp;block cipher加解密模式   
    1.  RGB 分別加密：   **mode_sep_encrypt.bmp** 
    2.  RGB 連續加密：   **mode_con_encrypt.bmp**
    3.  RGB 分別解密：   **mode_sep_decrypt.bmp**
    4.  RGB 連續解密：   **mode_con_decrypt.bmp**  
     