queries = {
    "metric_names": {
        "new": "INSERT INTO statbot.metric_names ( metric_name, creator_id, descr ) "
               "VALUES ( '{metric_name}', {user_id}, '{descr}');",
        "enable": "",
        "disable": ""
    },
    "users": {
        "create": "INSERT INTO statbot.users (user_id, firstname) VALUES ({user_id}, {firstname});",
        "check_id": "SELECT user_id, is_deleted FROM statbot.users WHERE user_id = {user_id};"
    }
}
