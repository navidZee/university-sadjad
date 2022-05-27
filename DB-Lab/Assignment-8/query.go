package main

import (
	"database/sql"
	"fmt"

	_ "github.com/go-sql-driver/mysql"
)

func main() {
	db, err := sql.Open("mysql")
	checkErr(err)
	stmt, err := db.Prepare("INSERT assets SET id=?,Assets Name=?,Unit Price=?,Count=?")
	checkErr(err)
	res, err := stmt.Exec("25", "restaurant", "2000 M", "55")
	checkErr(err)
	id, err := res.LastInsertId()
	checkErr(err)
	fmt.Println(id)
	stmt, err = db.Prepare("UPDATE assets SET Price=? where Id=?")
	checkErr(err)
	res, err = stmt.Exec("1,400 M", 1)
	checkErr(err)
	res, err = stmt.Exec("40 K", 2)
	checkErr(err)
	res, err = stmt.Exec("200 M", 3)
	checkErr(err)
	affect, err := res.RowsAffected()
	checkErr(err)
	fmt.Println(affect)

	stmt, err = db.Prepare("DELETE from assets where id=?")
	checkErr(err)
	res, err = stmt.Exec(2)
	checkErr(err)
	res, err = stmt.Exec(3)
	checkErr(err)
	affect, err = res.RowsAffected()
	checkErr(err)
	stmt, err := db.Prepare("INSERT assets SET id=?,Assets Name=?,Unit Price=?,Count=?")
	checkErr(err)
	res, err := stmt.Exec("2", "Cash", "40 K", "22500")
	checkErr(err)
	id, err := res.LastInsertId()
	checkErr(err)
	affect, err = res.RowsAffected()
	checkErr(err)
	fmt.Println(affect)
	stmt, err = db.Prepare("UPDATE assets SET Price=? where Id=?")
	checkErr(err)
	res, err = stmt.Exec("280 M", 2)
	checkErr(err)
	affect, err := res.RowsAffected()
	checkErr(err)
	stmt, err := db.Prepare("INSERT assets SET id=?,Assets Name=?,Unit Price=?,Count=?")
	checkErr(err)
	res, err := stmt.Exec("3", "EOS", "40 K", "5 K")
	checkErr(err)
	res, err := stmt.Exec("4", "ETH", "60 M", "7")
	checkErr(err)
	id, err := res.LastInsertId()
	checkErr(err)
	db.Close()
}

func checkErr(err error) {
	if err != nil {
		panic(err)
	}
}
