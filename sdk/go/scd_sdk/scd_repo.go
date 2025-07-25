package scd_sdk

import (
    "gorm.io/gorm"
)

type SCDModel interface {
    GetID() string
    GetVersion() int
    GetUID() string
}

type SCDRepository[T SCDModel] struct {
    db        *gorm.DB
    tableName string
}

func (r *SCDRepository[T]) FindLatest(filter func(*gorm.DB) *gorm.DB) ([]T, error) {
    var results []T
    sub := r.db.Table(r.tableName).
        Select("id, MAX(version) as max_version").
        Group("id")
    q := r.db.Table(r.tableName + " as t").
        Joins("JOIN (?) as latest ON latest.id = t.id AND latest.max_version = t.version", sub)
    if filter != nil {
        q = filter(q)
    }
    err := q.Find(&results).Error
    return results, err
}