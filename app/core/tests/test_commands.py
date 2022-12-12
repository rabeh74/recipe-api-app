from unittest.mock import patch # to simulate db(postgres)
# one of the error when we try connect to db 
from psycopg2 import OperationalError as psycopg2Error 
# allow us to call the command by the name
from django.core.management import call_command
#anothe error that may be througn by db
from django.db.utils import OperationalError
from django.test import SimpleTestCase
#mocking for check command and return patched_check (obj)
@patch('core.management.commands.wait_for_db.Command.check') # checl come from BaseCommand
class CommandTest(SimpleTestCase):
    """ test wiat db if db is ready """
    def test_wait_for_db_ready(self ,patched_check):
        patched_check.return_value=True
        # run code inside wait_for_db
        call_command('wait_for_db')

        #ensure that check method is called correctly with these coorect parameters (database)
        patched_check.assert_called_once_with(databases=['default'])
    @patch('time.sleep')
    def test_wait_for_db_delay(self , patched_sleep , patched_check):
        patched_check.side_effect = [psycopg2Error]*2 +\
            [OperationalError]*3 +[True]
        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])