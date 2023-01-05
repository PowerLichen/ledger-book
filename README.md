# 가계부(Ledger Book)
소비내역을 기록하고 관리할 수 있는 백엔드 서버.

## 구조
메인 디렉토리  
├── api  
│   ├── auth: 사용자 및 인증에 관한 코드  
│   ├── ledger: 가계부 CRUD에 관한 코드  
│   └── shortener: 단축 URL 생성 및 조회에 관한 코드  
│  
├── config: Django 메인 설정 파일  
│  
├── model  
│   ├── ledgermodel: 가계부 관련 모델  
│   ├── shortenermodel: 단축 URL 관련 모델  
│   └── usermodel: 사용자 관련 모델  
│  
├── database.sql: 데이터 베이스 DDL  
└── ...  
