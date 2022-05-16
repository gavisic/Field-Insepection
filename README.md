# Field-Insepection
Prerequisite
* Docker

Data Cleanup:
* changed column name ```inspection date``` to ```inspection_date``` and ```inspection time``` to  ```inspection_time```
* Assumption: all column are string
* format of file is xlxs

Steps to Run the  application
* ``` git clone https://github.com/gavisic/Field-Insepection ```
* ``` cd Field-Insepection ```
* ``` docker build -t  field-insepection . ```
* ``` docker run -d --name mycontainer -p 8000:8000 field-insepection ```

Application will run on ```http://localhost:8000```

APi:
* POST upload-record:
  ```http://localhost:8000/upload-record```
  
  body (form-data):
  ```file:<file path>```
  
 * GET upload-record:
  ```http://localhost:8000/get_record?appointment_id=01```
  
