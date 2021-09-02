import sqlite3

DB_PATH = "data.db"

# reactions (guild_id int, channel_id int, message_id int, reaction_id int, reaction_text text, is_custom_reaction int, role_id int)

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

def get_role_from_reaction(payload) -> int:
    if isinstance(payload.emoji, str):
        c.execute(
            f"SELECT role_id FROM reactions "
            f"WHERE guild_id={payload.guild_id} "
            f"AND channel_id={payload.channel_id} "
            f"AND message_id={payload.message_id} "
            f"AND is_custom_reaction=0 "
            f"AND reaction_text='{payload.emoji.name}';"
        )
    else:
        c.execute(
            f"SELECT role_id FROM reactions "
            f"WHERE guild_id={payload.guild_id} "
            f"AND channel_id={payload.channel_id} "
            f"AND message_id={payload.message_id} "
            f"AND is_custom_reaction=1 "
            f"AND reaction_id={payload.emoji.id};"
        )
    return c.fetchone()[0]

def add_reaction(guild_id, channel_id, message_id, reaction_id,
            reaction_text, is_custom_reaction, role_id) -> None:
    c.execute(f"INSERT INTO reactions VALUES("
        f"{guild_id},{channel_id},{message_id},{reaction_id},"
        f"'{reaction_text}',{is_custom_reaction},{role_id});"
    )
    conn.commit()

def remove_reaction(guild_id, channel_id, message_id, reaction_id,
            reaction_text, is_custom_reaction, role_id) -> None:
    c.execute(
        f"REMOVE FROM reactions "
        f"WHERE guild_id={guild_id} "
        f"AND channel_id={channel_id} "
        f"AND message_id={message_id} "
        f"AND reaction_id={reaction_id} "
        f"AND reaction_text={reaction_text} "
        f"AND is_custom_reaction={is_custom_reaction} "
        f"AND role_id={role_id};"
    )
    conn.commit()

def remove_reactions(payload) -> None:
    c.execute(
        f"DELETE FROM reactions "
        f"WHERE guild_id={payload.guild_id} "
        f"AND channel_id={payload.channel_id} "
        f"AND message_id={payload.message_id};"
    )
    conn.commit()