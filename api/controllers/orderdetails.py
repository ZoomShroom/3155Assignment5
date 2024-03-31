from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, orderdetail):
    db_orderdetail = models.OrderDetail(
        order_id=orderdetail.order_id,
        sandwich_id=orderdetail.sandwich_id,
        amount=orderdetail.amount
    )
    db.add(db_orderdetail)
    db.commit()
    db.refresh(db_orderdetail)
    return db_orderdetail


def read_all(db: Session):
    return db.query(models, models.OrderDetail).all()


def read_one(db: Session, orderdetail_id):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == orderdetail_id).first()


def update(db: Session, orderdetail_id, orderdetail):
    db_orderdetail = db.query(models.OrderDetail).filter(models.OrderDetail.id == orderdetail_id)
    update_data = orderdetail.model_dump(exclude_unset=True)
    db_orderdetail.update(update_data, synchronize_session=False)
    db.commit()
    return db_orderdetail.first()


def delete(db: Session, orderdetail_id):
    db_orderdetail = db.query(models.OrderDetail).filter(models.OrderDetail.id == orderdetail_id)
    db_orderdetail.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

