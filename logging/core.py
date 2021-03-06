

class Logger(object):
    def __init__(self, vigor: int = 0):
        self.vigor = vigor

        self.log_bot_init           : bool = False
        self.log_bot_reload         : bool = False
        self.log_bot_errors         : bool = False
        self.log_bot_warnings       : bool = False
        self.log_bot_left_srv       : bool = False
        self.log_bot_joined_srv     : bool = False

        self.log_cmd_exec           : bool = False
        self.log_cmd_exec_ct        : bool = False
        self.log_cmd_exec_err       : bool = False

        self.log_usr_left           : bool = False
        self.log_usr_joined         : bool = False
        self.log_usr_tag_changed    : bool = False
        self.log_usr_pfp_changed    : bool = False
        self.log_usr_name_changed   : bool = False
        self.log_usr_nick_changed   : bool = False

        self.log_msg_sent           : bool = False
        self.log_msg_edited         : bool = False
        self.log_msg_deleted        : bool = False

        self.log_srv_updated        : bool = False
        self.log_srv_inv_created    : bool = False
        self.log_srv_inv_deleted    : bool = False

        if self.vigor >= 0:
            self.log_bot_init         = True
            self.log_bot_reload       = True
            self.log_bot_errors       = True
            self.log_bot_warnings     = True
            self.log_cmd_exec         = True
            self.log_cmd_exec_err     = True
		
        if self.vigor >= 1:
            self.log_bot_left_srv     = True
            self.log_bot_joined_srv   = True
            self.log_usr_joined       = True
            self.log_usr_left         = True
            self.log_cmd_exec_ct      = True

        if self.vigor >= 2:
            self.log_usr_tag_changed  = True
            self.log_usr_pfp_changed  = True
            self.log_usr_name_changed = True
            self.log_usr_nick_changed = True
            self.log_msg_sent         = True
            self.log_msg_deleted      = True
            self.log_msg_edited       = True
            self.log_srv_updated      = True
            self.log_srv_inv_created  = True
            self.log_srv_inv_deleted  = True
