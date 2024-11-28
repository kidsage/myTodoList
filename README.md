# myTodoList
 - todo app 백엔드 구조를 만들어보는 연습용 리포지토리. (수정일자 11/28)

* * *
## 모델 관계
- app
  - Board
      > 필드: id, name, description, owner (User), created_at, updated_at  
      > 관계: Board → List (One-to-Many)
  
  - List
      > 필드: id, name, position, board (ForeignKey to Board), created_at, updated_at  
      > 관계: List → Card (One-to-Many)
  
  - Card
      > 필드: id, title, description, due_date, position, list (ForeignKey to List), assignee (ForeignKey to User), created_at, updated_at  
      > 관계: Card → Comment (One-to-Many)  
      >      Card → Attachment (One-to-Many)
  
  - Comment
      > 필드: id, text, author (ForeignKey to User), card (ForeignKey to Card), created_at, updated_at  
      > 관계: Comment → Card (Many-to-One)  
  
  - Attachment
      > 필드: id, file, name, card (ForeignKey to Card), uploaded_at  
      > 관계: Attachment → Card (Many-to-One)  

- 전체 연결구조
    > User (Django 기본 모델)  
    &emsp;↳ Board.owner (ForeignKey)  
    &emsp;↳ Card.assignee (ForeignKey)  
    &emsp;↳ Comment.author (ForeignKey)  
    > Board  
    &emsp;↳ List.board (One-to-Many)  
    > List  
    &emsp;↳ Card.list (One-to-Many)  
    > Card  
    &emsp;↳ Comment.card (One-to-Many)
    &emsp;↳ Attachment.card (One-to-Many)  

