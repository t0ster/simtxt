from bson import ObjectId

from simtxt.orm import Text


def test_orm():
    result = Text.from_db(
        content="hello",
        created=1231312,
        _id=ObjectId(),
        sentences=[{"_id": ObjectId(), "textId": ObjectId(), "content": "Hello world"}],
    )
    assert "created" not in result
    assert isinstance(result["id"], str)
