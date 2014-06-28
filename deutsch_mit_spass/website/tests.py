from django.test import TestCase
from django.contrib.auth.models import User
from website.models import CorrectingExercise, TranslationExercise,\
    UserProfile, ReadingExercise, FillInExercise, OrderingExercise


class DeutschMitSpassCase(TestCase):

    def test_index(self):
        resp = self.client.get('/website/')
        self.assertEqual(resp.status_code, 200)
#       request is anonymous
        self.assertTrue('username' not in resp.context)

    def test_login_view(self):
        resp = self.client.get('/website/login')
        self.assertEqual(resp.status_code, 200)
#       request is anonymous
        self.assertTrue('username' not in resp.context)

    def test_register_view(self):
        resp = self.client.get('/website/register')
        self.assertEqual(resp.status_code, 200)
#       request is anonymous
        self.assertTrue('username' not in resp.context)

    def test_do_translations(self):
        resp = self.client.get('/website/dotranslations')
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(None, resp.context)

    def test_do_corrections(self):
        resp = self.client.get('/website/docorrections')
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(None, resp.context)

    def test_do_exercise(self):
        resp = self.client.get('/website/doexercises')
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(None, resp.context)

    def test_add_translation(self):
        resp = self.client.get('/website/translation')
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(None, resp.context)

    def test_add_correction(self):
        resp = self.client.get('/website/correction')
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(None, resp.context)

    def test_add_exercise(self):
        resp = self.client.get('/website/exercises')
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(None, resp.context)


class DeutchMitSpassLoggedInStudent(TestCase):
    def setUp(self):
        self.username = 'test'
        self.email = 'test@test.com'
        self.password = 'test'
        self.test_user = User.objects.create_user(
            self.username,
            self.email,
            self.password)
        self.test_user_profile = UserProfile()
        self.test_user_profile.user = self.test_user
        self.test_user_profile.role = UserProfile.STUDENT
        self.test_user_profile.save()
        login = self.client.login(
            username=self.username,
            password=self.password)
        self.assertEqual(login, True)

    def test_doexercises(self):
        resp = self.client.get('/website/doexercises')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('username' in resp.context)
        self.assertEqual(resp.context['username'], 'test')

    def test_dotranslations(self):
        resp = self.client.get('/website/dotranslations')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('translation_exercises' in resp.context)
        self.assertTrue('username' in resp.context)
        self.assertEqual(resp.context['username'], 'test')

    def test_dotranslations_exercise_correct(self):
        exercise = TranslationExercise()
        exercise.translated_example = 'very good'
        exercise.example = 'sehr gut'
        exercise.save()
        self.assertEquals(len(TranslationExercise.objects.all()), 1)
        resp = self.client.post('/website/dotranslations', {
            'answer': 'sehr gut', 'id': '1'})
        self.assertEquals(resp.content, b'correct')

    def test_docorrections(self):
        resp = self.client.get('/website/docorrections')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('correcting_exercises' in resp.context)
        self.assertTrue('username' in resp.context)
        self.assertEqual(resp.context['username'], 'test')

    def test_docorrection_exercise_correct(self):
        exercise = CorrectingExercise()
        exercise.correct_sentence = 'nicht schlecht'
        exercise.wrong_sentence = 'nein schlecht'
        exercise.save()
        self.assertEquals(len(CorrectingExercise.objects.all()), 1)
        resp = self.client.post('/website/docorrections', {
            'answer': 'nicht schlecht', 'id': '1'})
        self.assertEquals(resp.content, b'correct')

    def test_dofillin_exercise_correct(self):
        exercise = FillInExercise()
        exercise.example = 'test *** test'
        exercise.correct_answer = 'ja'
        exercise.wrong_answer = 'nein'
        exercise.second_wrong_answer = 'nein nein'
        exercise.save()
        self.assertEquals(len(FillInExercise.objects.all()), 1)
        resp = self.client.post('/website/dofillins', {
            'answer': 'ja', 'id': '1'})
        self.assertEquals(resp.content, b'correct')
        wrong_resp = self.client.post('/website/dofillins', {
            'answer': 'ja', 'id': '1'})
        self.assertEquals(wrong_resp.content, b'correct')

    def test_doreadings(self):
        resp = self.client.get('/website/doreading')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('reading_exercises' in resp.context)
        self.assertTrue('username' in resp.context)
        self.assertEqual(resp.context['username'], 'test')

    def test_access_exercises(self):
        resp = self.client.get('/website/exercises')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('role' in resp.context)
        self.assertTrue('username' in resp.context)
        self.assertEqual(resp.context['username'], 'test')
        self.assertEqual(resp.context['role'], 'Student')

    def test_access_add_corrections(self):
        resp = self.client.get('/website/correction')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('role' in resp.context)
        self.assertEqual(resp.context['role'], 'Student')
        self.client.post('/website/correction', {
            'correct_sentence': 'should not add',
            'second_correct_sentence': 'should not add',
            'wrong_sentence': 'should not be added'})
#       student should not add exercises
        self.assertEqual(len(CorrectingExercise.objects.all()), 0)

    def test_access_add_translations(self):
        resp = self.client.get('/website/translation')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('role' in resp.context)
        self.assertEqual(resp.context['role'], 'Student')
        self.client.post('/website/translation', {
            'example': 'should not add',
            'translated_example': 'should not add'})
#       student should not add exercises
        self.assertEqual(len(TranslationExercise.objects.all()), 0)

    def test_access_add_readings(self):
        resp = self.client.get('/website/reading')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('role' in resp.context)
        self.assertEqual(resp.context['role'], 'Student')
        self.client.post('/website/reading', {
            'text': 'Lorem ipsum .......................',
            'question': 'Ist das text ohne Wert',
            'first_choise': 'Ja',
            'first_is_correct': '1',
            'second_choise': 'Nein',
            'second_is_correct': '0',
            'third_choise': 'Nein',
            'third_is_correct': '0',
            'fourt_choise': 'Nein',
            'fourt_is_correct': '0'
            })
#       student should not add exercises
        self.assertEqual(len(ReadingExercise.objects.all()), 0)

    def test_access_add_fillin(self):
        resp = self.client.get('/website/fillin')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('role' in resp.context)
        self.assertEqual(resp.context['role'], 'Student')
        self.client.post('/website/fillin', {
            'example': 'Du *** gut',
            'correct_answer': 'bist',
            'wrong_answer': 'ist',
            'second_wrong_answer': 'hast'
            })
#       student should not add exercises
        self.assertEqual(len(FillInExercise.objects.all()), 0)

    def test_access_add_ordering(self):
        resp = self.client.get('/website/ordering')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('role' in resp.context)
        self.assertEqual(resp.context['role'], 'Student')
        self.client.post('/website/ordering', {
            'description': 'test',
            'first': 'test1',
            'second': 'test2',
            'third': 'test3',
            'fourt': 'test4',
            'first_match': 'test11',
            'second_match': 'test22',
            'third_match': 'test33',
            'fourt_match': 'test44',
            })
#       student should not add exercises
        self.assertEqual(len(OrderingExercise.objects.all()), 0)


class DeutchMitSpassLoggedInTeacher(TestCase):
    def setUp(self):
        self.username = 'test'
        self.email = 'test@test.com'
        self.password = 'test'
        self.test_user = User.objects.create_user(
            self.username,
            self.email,
            self.password)
        self.test_user_profile = UserProfile()
        self.test_user_profile.user = self.test_user
        self.test_user_profile.role = UserProfile.TEACHER
        self.test_user_profile.save()
        login = self.client.login(
            username=self.username,
            password=self.password)
        self.assertEqual(login, True)

    def test_doexercises(self):
        resp = self.client.get('/website/doexercises')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('username' in resp.context)
        self.assertEqual(resp.context['username'], 'test')

    def test_dotranslations(self):
        resp = self.client.get('/website/dotranslations')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('translation_exercises' in resp.context)
        self.assertTrue('username' in resp.context)
        self.assertEqual(resp.context['username'], 'test')

    def test_dotranslations_exercise_correct(self):
        exercise = TranslationExercise()
        exercise.translated_example = 'very good'
        exercise.example = 'sehr gut'
        exercise.save()
        self.assertEquals(len(TranslationExercise.objects.all()), 1)
        resp = self.client.post('/website/dotranslations', {
            'answer': 'sehr gut', 'id': '1'})
        self.assertEquals(resp.content, b'correct')

    def test_docorrections(self):
        resp = self.client.get('/website/docorrections')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('correcting_exercises' in resp.context)
        self.assertTrue('username' in resp.context)
        self.assertEqual(resp.context['username'], 'test')

    def test_docorrection_exercise_correct(self):
        exercise = CorrectingExercise()
        exercise.correct_sentence = 'nicht schlecht'
        exercise.wrong_sentence = 'nein schlecht'
        exercise.save()
        self.assertEquals(len(CorrectingExercise.objects.all()), 1)
        resp = self.client.post('/website/docorrections', {
            'answer': 'nicht schlecht', 'id': '1'})
        self.assertEquals(resp.content, b'correct')

    def test_access_exercises(self):
        resp = self.client.get('/website/exercises')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('role' in resp.context)
        self.assertTrue('username' in resp.context)
        self.assertEqual(resp.context['username'], 'test')
        self.assertEqual(resp.context['role'], 'Teacher')

    def test_access_add_corrections(self):
        resp = self.client.get('/website/correction')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('role' in resp.context)
        self.assertEqual(resp.context['role'], 'Teacher')
        self.client.post('/website/correction', {
            'correct_sentence': 'should be added',
            'second_correct_sentence': 'should be added',
            'wrong_sentence': 'should be add'})
#       teacher should be able to add exercises
        self.assertEqual(len(CorrectingExercise.objects.all()), 1)

    def test_access_add_translations(self):
        resp = self.client.get('/website/translation')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('role' in resp.context)
        self.assertEqual(resp.context['role'], 'Teacher')
        self.client.post('/website/translation', {
            'example': 'should add',
            'translated_example': 'should add'})
#       teacher should be able to add exercises
        self.assertEqual(len(TranslationExercise.objects.all()), 1)

    def test_access_add_readings(self):
        resp = self.client.get('/website/reading')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('role' in resp.context)
        self.assertEqual(resp.context['role'], 'Teacher')
        resp_post = self.client.post('/website/reading', {
            'text': 'Lorem ipsum .......................',
            'question': 'Ist das text ohne Wert',
            'first_choise': 'Ja',
            'first_is_correct': '1',
            'second_choise': 'Nein',
            'second_is_correct': '0',
            'third_choise': 'Nein',
            'third_is_correct': '0',
            'fourt_choise': 'Nein',
            'fourt_is_correct': '0'
            })
#       teacher should be able to add exercises
        self.assertEqual(len(ReadingExercise.objects.all()), 1)
        self.assertEqual(resp_post.status_code, 200)

    def test_doreadings_exercise_correct(self):
        self.client.post('/website/reading', {
            'text': 'Lorem ipsum .......................',
            'question': 'Ist das text ohne Wert',
            'first_choise': 'Ja',
            'first_is_correct': '1',
            'second_choise': 'Nein',
            'second_is_correct': '0',
            'third_choise': 'Nein',
            'third_is_correct': '0',
            'fourt_choise': 'Nein',
            'fourt_is_correct': '0'
            })
        self.assertEquals(len(ReadingExercise.objects.all()), 1)
        resp = self.client.post('/website/doreading', {
            'answer': 'Ja', 'id': '1'})
        self.assertEquals(resp.content, b'correct')

    def test_access_add_fillin(self):
        resp = self.client.get('/website/fillin')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('role' in resp.context)
        self.assertEqual(resp.context['role'], 'Teacher')
        self.client.post('/website/fillin', {
            'example': 'Du *** gut',
            'correct_answer': 'bist',
            'wrong_answer': 'ist',
            'second_wrong_answer': 'hast'
            })
#       teacher should be able to add exercises
        self.assertEqual(len(FillInExercise.objects.all()), 1)

    def test_access_add_ordering(self):
        resp = self.client.get('/website/ordering')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('role' in resp.context)
        self.assertEqual(resp.context['role'], 'Teacher')
        self.client.post('/website/ordering', {
            'description': 'test',
            'first': 'test1',
            'second': 'test2',
            'third': 'test3',
            'fourt': 'test4',
            'first_match': 'test11',
            'second_match': 'test22',
            'third_match': 'test33',
            'fourt_match': 'test44',
            })
#       teacher should be able to add exercises
        self.assertEqual(len(OrderingExercise.objects.all()), 1)

    def test_doordering_exercise_correct(self):
        self.client.post('/website/ordering', {
            'description': 'test',
            'first': 'test1',
            'second': 'test2',
            'third': 'test3',
            'fourt': 'test4',
            'first_match': 'test11',
            'second_match': 'test22',
            'third_match': 'test33',
            'fourt_match': 'test44',
            })
        self.assertEquals(len(OrderingExercise.objects.all()), 1)
        resp = self.client.post('/website/doorderings', {
            'first': 'test11',
            'second': 'test22',
            'third': 'test33',
            'fourt': 'test44',
            'id': '1'})
        self.assertEquals(resp.content, b'correct')
