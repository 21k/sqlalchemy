package main
import (
    "os"
    "fmt"
    "github.com/jinzhu/gorm"
    _ "github.com/jinzhu/gorm/dialects/mysql"
  )
  type User struct {
    Id         string
    Username   string 
    CreateTime  string
  }

  func (User) TableName() string {
    return "user"
  }

  func main() {
    var users = []User{}
    var order_by = os.Args[1]
    db, _ := gorm.Open("mysql", "root@tcp(127.0.0.1:3306)/sql_test")
    db.Order(order_by).Find(&users)
    fmt.Println(users)
  }
