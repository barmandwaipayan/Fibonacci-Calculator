from django.test import TestCase
from .models import NFibo
from rest_framework.test import APIClient
from .serializers import NFiboSerializer
from rest_framework.renderers import JSONRenderer

# Create your tests here.

class ModelTestCase(TestCase):
    def setUp(self):
        """Define the test client and other test variables."""
        self.fibo_test = NFibo(number = 1234567, fibo = "123456789123456789123456789123456789")

    def test_model_can_create_a_record(self):
        """Test if NFibo model can create a record."""
        old_count = NFibo.objects.count()
        self.fibo_test.save()
        new_count = NFibo.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_pk(self):
        """Test if NFibo model has number as PK."""
        self.fibo_test.save()
        old_count = NFibo.objects.count()
        self.fibo_test = NFibo(number = 1234567, fibo = "11")
        self.fibo_test.save()
        new_count = NFibo.objects.count()
        self.assertEqual(old_count, new_count)


class APITestCase(TestCase):
    """Test suite for the api output and logic."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.factory = APIClient()
        self.Values = ['1','2','10','100','502', '2565', '10000']
        self.Fibos = ["""1""", """1""", """55""", """354224848179261915075""", """365014740723634211012237077906479355996081581501455497852747829366800199361550174096573645929019489792751""",
         """50560602325211320276308442786174323816418503110343173339881037521319242565879986873970909075454794657072630118858286917983885429850706528435958814055707218537438340872853116221389494451068253066179337272230841505621941958827523921341950999344994314583008328386062377503525302143333229324915465696120737279764162253845772738498966437241044809042918628484895934807662546989978152502014880283997784552051154894441638000757411783840665277765237296278594104010108484722551973564300846298980374255370923698745697857697732549127771469660570690""",
          """33644764876431783266621612005107543310302148460680063906564769974680081442166662368155595513633734025582065332680836159373734790483865268263040892463056431887354544369559827491606602099884183933864652731300088830269235673613135117579297437854413752130520504347701602264758318906527890855154366159582987279682987510631200575428783453215515103870818298969791613127856265033195487140214287532698187962046936097879900350962302291026368131493195275630227837628441540360584402572114334961180023091208287046088923962328835461505776583271252546093591128203925285393434620904245248929403901706233888991085841065183173360437470737908552631764325733993712871937587746897479926305837065742830161637408969178426378624212835258112820516370298089332099905707920064367426202389783111470054074998459250360633560933883831923386783056136435351892133279732908133732642652633989763922723407882928177953580570993691049175470808931841056146322338217465637321248226383092103297701648054726243842374862411453093812206564914032751086643394517512161526545361333111314042436854805106765843493523836959653428071768775328348234345557366719731392746273629108210679280784718035329131176778924659089938635459327894523777674406192240337638674004021330343297496902028328145933418826817683893072003634795623117103101291953169794607632737589253530772552375943788434504067715555779056450443016640119462580972216729758615026968443146952034614932291105970676243268515992834709891284706740862008587135016260312071903172086094081298321581077282076353186624611278245537208532365305775956430072517744315051539600905168603220349163222640885248852433158051534849622434848299380905070483482449327453732624567755879089187190803662058009594743150052402532709746995318770724376825907419939632265984147498193609285223945039707165443156421328157688908058783183404917434556270520223564846495196112460268313970975069382648706613264507665074611512677522748621598642530711298441182622661057163515069260029861704945425047491378115154139941550671256271197133252763631939606902895650288268608362241082050562430701794976171121233066073310059947366875"""]


    def test_api_fetch_and_logic(self):
        current_url = "http://127.0.0.1:8000/getfibo/"
        for i in range(3):
            url = current_url + str(self.Values[i]) + '/'
            response = self.client.get(url)
            test_result = []
            test_result.append(NFibo(number = self.Values[i], fibo = self.Fibos[i]))
            test_result = NFiboSerializer(test_result, many=True)
            test_result = JSONRenderer().render(test_result.data)
            """Same formatting for comparing"""
            self.assertEqual(JSONRenderer().render(response.json()), test_result)