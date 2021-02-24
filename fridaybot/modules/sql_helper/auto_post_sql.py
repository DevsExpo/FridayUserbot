import threading

from sqlalchemy import Column, String, UnicodeText, distinct, func

from . import BASE, SESSION


class Post(BASE):
    __tablename__ = "post"
    target_chat_id = Column(String(14), primary_key=True)
    to_post_chat_id = Column(String(14), primary_key=True, nullable=False)

    def __init__(self, target_chat_id, to_post_chat_id):
        self.to_post_chat_id = str(to_post_chat_id)
        self.target_chat_id = str(target_chat_id)

    def __repr__(self):
        return "<Auto post filter '%s' for %s>" % (self.target_chat_id, self.to_post_chat_id)

    def __eq__(self, other):
        return bool(
            isinstance(other, Post)
            and self.target_chat_id == other.target_chat_id
            and self.to_post_chat_id == other.to_post_chat_id
        )

        


Post.__table__.create(checkfirst=True)

POST_FILTER_INSERTION_LOCK = threading.RLock()

CHAT_POSTS = {}

def add_new_post_data_in_db(target_chat_id: str, to_post_chat_id: str):
    with POST_FILTER_INSERTION_LOCK:
        blacklist_filt = Post(str(target_chat_id), str(to_post_chat_id))

        SESSION.merge(blacklist_filt)  
        SESSION.commit()
        CHAT_POSTS.setdefault(str(target_chat_id), set()).add(str(to_post_chat_id))


def get_all_post_data(target_chat_id: str):
    return CHAT_POSTS.get(str(target_chat_id), set())


def is_post_data_in_db(target_chat_id, to_post_chat_id):
    with POST_FILTER_INSERTION_LOCK:
        broadcast_group = SESSION.query(Post).get((str(target_chat_id), str(to_post_chat_id)))
        return bool(broadcast_group)


def remove_post_data(target_chat_id, to_post_chat_id):
    with POST_FILTER_INSERTION_LOCK:
        blacklist_filt = SESSION.query(Post).get((str(target_chat_id), str(to_post_chat_id)))
        if blacklist_filt:
            if str(to_post_chat_id) in CHAT_POSTS.get(str(target_chat_id), set()):  # sanity check
                CHAT_POSTS.get(str(target_chat_id), set()).remove(str(to_post_chat_id))

            SESSION.delete(blacklist_filt)
            SESSION.commit()
            return True

        SESSION.close()
        return False

def __load_chat_channels():
    global CHAT_POSTS
    try:
        chats = SESSION.query(Post.target_chat_id).distinct().all()
        for (target_chat_id,) in chats: 
            CHAT_POSTS[target_chat_id] = []

        all_filters = SESSION.query(Post).all()
        for x in all_filters:
            CHAT_POSTS[x.target_chat_id] += [x.to_post_chat_id]

        CHAT_POSTS = {x: set(y) for x, y in CHAT_POSTS.items()}

    finally:
        SESSION.close()


__load_chat_channels()        
