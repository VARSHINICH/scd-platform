package main

import (
    "scd_sdk"
    "gorm.io/gorm"
)

func main() {
    var db *gorm.DB // initialize your DB
    jobRepo := scd_sdk.SCDRepository[Job]{db: db, tableName: "jobs"}
    activeJobs, err := jobRepo.FindLatest(func(db *gorm.DB) *gorm.DB {
        return db.Where("status = ?", "active").Where("company_id = ?", "comp_123")
    })
    // handle activeJobs and err
}