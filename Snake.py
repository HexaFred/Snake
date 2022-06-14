from tkinter import*
from random import*
import random
import pygame.mixer
pygame.mixer.init()

#les variables
dx=0
dy=0
dx1=0
dy1=0
dx1bis=0
dy1bis=0
dd1=1
dd2=0
dx2=0
dy2=0
dx2bis=0
dy2bis=0
dx3bis=0
dy3bis=0
dx3=0
dy3=0
dx4=0
dy4=0
dx4bis=0
dy4bis=0
dx5=0
dy5=0
dx5bis=0
dy5bis=0
dx6=0
dy6=0
dx6bis=0
dy6bis=0
dx7=0
dy7=0
dx7bis=0
dy7bis=0
dx8=0
dy8=0
dx8bis=0
dy8bis=0
dx9=0
dy9=0
dx9bis=0
dy9bis=0
dx10=0
dy10=0
dx10bis=0
dy10bis=0
dx11=0
dy11=0
dx11bis=0
dy11bis=0
dx12=0
dy12=0
dx12bis=0
dy12bis=0
dx13=0
dy13=0
dx13bis=0
dy13bis=0
dx14=0
dy14=0
dx14bis=0
dy14bis=0
dx15=0
dy15=0
dx15bis=0
dy15bis=0
dx16=0
dy16=0
dx16bis=0
dy16bis=0
dx17=0
dy17=0
dx17bis=0
dy17bis=0
dx18=0
dy18=0
dx18bis=0
dy18bis=0
dx19=0
dy19=0
dx19bis=0
dy19bis=0
dx20=0
dy20=0
dx20bis=0
dy20bis=0
dx21=0
dy21=0
dx21bis=0
dy21bis=0
dx22=0
dy22=0
dx22bis=0
dy22bis=0
dx23=0
dy23=0
dx23bis=0
dy23bis=0
dx24=0
dy24=0
dx24bis=0
dy24bis=0
dx25=0
dy25=0
dx25bis=0
dy25bis=0
dx26=0
dy26=0
dx26bis=0
dy26bis=0
dx27=0
dy27=0
dx27bis=0
dy27bis=0
dx28=0
dy28=0
dx28bis=0
dy28bis=0
dx29=0
dy29=0
dx29bis=0
dy29bis=0
dx30=0
dy30=0
dx30bis=0
dy30bis=0
dx31=0
dy31=0
dx31bis=0
dy31bis=0
dx32=0
dy32=0
dx32bis=0
dy32bis=0
dx33=0
dy33=0
dx33bis=0
dy33bis=0
dx34=0
dy34=0
dx34bis=0
dy34bis=0
dx35=0
dy35=0
dx35bis=0
dy35bis=0
dx36=0
dy36=0
dx36bis=0
dy36bis=0
dx37=0
dy37=0
dx37bis=0
dy37bis=0
dx38=0
dy38=0
dx38bis=0
dy38bis=0
dx39=0
dy39=0
dx39bis=0
dy39bis=0
dx40=0
dy40=0
dx40bis=0
dy40bis=0
dx41=0
dy41=0
dx41bis=0
dy41bis=0
dx42=0
dy42=0
dx42bis=0
dy42bis=0
dx43=0
dy43=0
dx43bis=0
dy43bis=0
dx44=0
dy44=0
dx44bis=0
dy44bis=0
dx45=0
dy45=0
dx45bis=0
dy45bis=0
dx46=0
dy46=0
dx46bis=0
dy46bis=0
dx47=0
dy47=0
dx47bis=0
dy47bis=0
dx48=0
dy48=0
dx48bis=0
dy48bis=0
dx49=0
dy49=0
dx49bis=0
dy49bis=0
dx50=0
dy50=0
dx50bis=0
dy50bis=0
dx51=0
dy51=0
dx51bis=0
dy51bis=0
dx52=0
dy52=0
dx52bis=0
dy52bis=0
dx53=0
dy53=0
dx53bis=0
dy53bis=0
dx54=0
dy54=0
dx54bis=0
dy54bis=0
dx55=0
dy55=0
dx55bis=0
dy55bis=0
dx56=0
dy56=0
dx56bis=0
dy56bis=0
dx57=0
dy57=0
dx57bis=0
dy57bis=0
dx58=0
dy58=0
dx58bis=0
dy58bis=0
dx59=0
dy59=0
dx59bis=0
dy59bis=0
dx60=0
dy60=0
dx60bis=0
dy60bis=0
dx61=0
dy61=0
dx61bis=0
dy61bis=0
dx62=0
dy62=0
dx62bis=0
dy62bis=0
dx63=0
dy63=0
dx63bis=0
dy63bis=0
dx64=0
dy64=0
dx64bis=0
dy64bis=0
dx65=0
dy65=0
dx65bis=0
dy65bis=0
dx66=0
dy66=0
dx66bis=0
dy66bis=0
dx67=0
dy67=0
dx67bis=0
dy67bis=0
dx68=0
dy68=0
dx68bis=0
dy68bis=0
dx69=0
dy69=0
dx69bis=0
dy69bis=0
dx70=0
dy70=0
dx70bis=0
dy70bis=0
dx71=0
dy71=0
dx71bis=0
dy71bis=0
dx72=0
dy72=0
dx72bis=0
dy72bis=0
dx73=0
dy73=0
dx73bis=0
dy73bis=0
dx74=0
dy74=0
dx74bis=0
dy74bis=0
dx75=0
dy75=0
dx75bis=0
dy75bis=0
dx76=0
dy76=0
dx76bis=0
dy76bis=0
dx77=0
dy77=0
dx77bis=0
dy77bis=0
dx78=0
dy78=0
dx78bis=0
dy78bis=0
dx79=0
dy79=0
dx79bis=0
dy79bis=0
dx80=0
dy80=0
dx80bis=0
dy80bis=0
dx81=0
dy81=0
dx81bis=0
dy81bis=0
dx82=0
dy82=0
dx82bis=0
dy82bis=0
dx83=0
dy83=0
dx83bis=0
dy83bis=0
dx84=0
dy84=0
dx84bis=0
dy84bis=0
dx85=0
dy85=0
dx85bis=0
dy85bis=0
dx86=0
dy86=0
dx86bis=0
dy86bis=0
dx87=0
dy87=0
dx87bis=0
dy87bis=0
dx88=0
dy88=0
dx88bis=0
dy88bis=0
dx89=0
dy89=0
dx89bis=0
dy89bis=0
dx90=0
dy90=0
dx90bis=0
dy90bis=0
dx91=0
dy91=0
dx91bis=0
dy91bis=0
dx92=0
dy92=0
dx92bis=0
dy92bis=0
dx93=0
dy93=0
dx93bis=0
dy93bis=0
dx94=0
dy94=0
dx94bis=0
dy94bis=0
dx95=0
dy95=0
dx95bis=0
dy95bis=0
dx96=0
dy96=0
dx96bis=0
dy96bis=0
dx97=0
dy97=0
dx97bis=0
dy97bis=0
dx98=0
dy98=0
dx98bis=0
dy98bis=0
dx99=0
dy99=0
dx99bis=0
dy99bis=0
dx100=0
dy100=0
dx100bis=0
dy100bis=0
dx101=0
dy101=0
dx101bis=0
dy101bis=0
dx102=0
dy102=0
dx102bis=0
dy102bis=0
dx103=0
dy103=0
dx103bis=0
dy103bis=0
dx104=0
dy104=0
dx104bis=0
dy104bis=0
dx105=0
dy105=0
dx105bis=0
dy105bis=0
dx106=0
dy106=0
dx106bis=0
dy106bis=0
dx107=0
dy107=0
dx107bis=0
dy107bis=0
dx108=0
dy108=0
dx108bis=0
dy108bis=0
dx109=0
dy109=0
dx109bis=0
dy109bis=0
dx110=0
dy110=0
dx110bis=0
dy110bis=0
dx111=0
dy111=0
dx111bis=0
dy111bis=0
dx112=0
dy112=0
dx112bis=0
dy112bis=0
dx113=0
dy113=0
dx113bis=0
dy113bis=0
dx114=0
dy114=0
dx114bis=0
dy114bis=0
dx115=0
dy115=0
dx115bis=0
dy115bis=0
dx116=0
dy116=0
dx116bis=0
dy116bis=0
dx117=0
dy117=0
dx117bis=0
dy117bis=0
dx118=0
dy118=0
dx118bis=0
dy118bis=0
dx119=0
dy119=0
dx119bis=0
dy119bis=0
dx120=0
dy120=0
dx120bis=0
dy120bis=0
dx121=0
dy121=0
dx121bis=0
dy121bis=0
dx122=0
dy122=0
dx122bis=0
dy122bis=0
dx123=0
dy123=0
dx123bis=0
dy123bis=0
dx124=0
dy124=0
dx124bis=0
dy124bis=0
dx125=0
dy125=0
dx125bis=0
dy125bis=0
dx126=0
dy126=0
dx126bis=0
dy126bis=0
dx127=0
dy127=0
dx127bis=0
dy127bis=0
dx128=0
dy128=0
dx128bis=0
dy128bis=0
dx129=0
dy129=0
dx129bis=0
dy129bis=0
dx130=0
dy130=0
dx130bis=0
dy130bis=0
dx131=0
dy131=0
dx131bis=0
dy131bis=0
dx132=0
dy132=0
dx132bis=0
dy132bis=0
dx133=0
dy133=0
dx133bis=0
dy133bis=0
dx134=0
dy134=0
dx134bis=0
dy134bis=0
dx135=0
dy135=0
dx135bis=0
dy135bis=0
dx136=0
dy136=0
dx136bis=0
dy136bis=0
dx137=0
dy137=0
dx137bis=0
dy137bis=0
dx138=0
dy138=0
dx138bis=0
dy138bis=0
dx139=0
dy139=0
dx139bis=0
dy139bis=0
dx140=0
dy140=0
dx140bis=0
dy140bis=0
dx141=0
dy141=0
dx141bis=0
dy141bis=0
dx142=0
dy142=0
dx142bis=0
dy142bis=0
dx143=0
dy143=0
dx143bis=0
dy143bis=0
dx144=0
dy144=0
dx144bis=0
dy144bis=0
dx145=0
dy145=0
dx145bis=0
dy145bis=0
dx146=0
dy146=0
dx146bis=0
dy146bis=0
dx147=0
dy147=0
dx147bis=0
dy147bis=0
dx148=0
dy148=0
dx148bis=0
dy148bis=0
dx149=0
dy149=0
dx149bis=0
dy149bis=0
dx150=0
dy150=0
dx150bis=0
dy150bis=0
dx151=0
dy151=0
dx151bis=0
dy151bis=0
dx152=0
dy152=0
dx152bis=0
dy152bis=0
dx153=0
dy153=0
dx153bis=0
dy153bis=0
dx154=0
dy154=0
dx154bis=0
dy154bis=0
dx155=0
dy155=0
dx155bis=0
dy155bis=0
dx156=0
dy156=0
dx156bis=0
dy156bis=0
dx157=0
dy157=0
dx157bis=0
dy157bis=0
dx158=0
dy158=0
dx158bis=0
dy158bis=0
dx159=0
dy159=0
dx159bis=0
dy159bis=0
dx160=0
dy160=0
dx160bis=0
dy160bis=0
dx161=0
dy161=0
dx161bis=0
dy161bis=0
dx162=0
dy162=0
dx162bis=0
dy162bis=0
dx163=0
dy163=0
dx163bis=0
dy163bis=0
dx164=0
dy164=0
dx164bis=0
dy164bis=0
dx165=0
dy165=0
dx165bis=0
dy165bis=0
dx166=0
dy166=0
dx166bis=0
dy166bis=0
dx167=0
dy167=0
dx167bis=0
dy167bis=0
dx168=0
dy168=0
dx168bis=0
dy168bis=0
dx169=0
dy169=0
dx169bis=0
dy169bis=0
dx170=0
dy170=0
dx170bis=0
dy170bis=0
dx171=0
dy171=0
dx171bis=0
dy171bis=0
dx172=0
dy172=0
dx172bis=0
dy172bis=0
dx173=0
dy173=0
dx173bis=0
dy173bis=0
dx174=0
dy174=0
dx174bis=0
dy174bis=0
dx175=0
dy175=0
dx175bis=0
dy175bis=0
dx176=0
dy176=0
dx176bis=0
dy176bis=0
dx177=0
dy177=0
dx177bis=0
dy177bis=0
dx178=0
dy178=0
dx178bis=0
dy178bis=0
dx179=0
dy179=0
dx179bis=0
dy179bis=0
dx180=0
dy180=0
dx180bis=0
dy180bis=0
dx181=0
dy181=0
dx181bis=0
dy181bis=0
dx182=0
dy182=0
dx182bis=0
dy182bis=0
dx183=0
dy183=0
dx183bis=0
dy183bis=0
dx184=0
dy184=0
dx184bis=0
dy184bis=0
dx185=0
dy185=0
dx185bis=0
dy185bis=0
dx186=0
dy186=0
dx186bis=0
dy186bis=0
dx187=0
dy187=0
dx187bis=0
dy187bis=0
dx188=0
dy188=0
dx188bis=0
dy188bis=0
dx189=0
dy189=0
dx189bis=0
dy189bis=0
dx190=0
dy190=0
dx190bis=0
dy190bis=0
dx191=0
dy191=0
dx191bis=0
dy191bis=0
dx192=0
dy192=0
dx192bis=0
dy192bis=0
dx193=0
dy193=0
dx193bis=0
dy193bis=0
dx194=0
dy194=0
dx194bis=0
dy194bis=0
dx195=0
dy195=0
dx195bis=0
dy195bis=0
dx196=0
dy196=0
dx196bis=0
dy196bis=0
dx197=0
dy197=0
dx197bis=0
dy197bis=0
dx198=0
dy198=0
dx198bis=0
dy198bis=0
dx199=0
dy199=0
dx199bis=0
dy199bis=0
dx200=0
dy200=0
dx200bis=0
dy200bis=0
dx201=0
dy201=0
dx201bis=0
dy201bis=0
dx202=0
dy202=0
dx202bis=0
dy202bis=0
dx203=0
dy203=0
dx203bis=0
dy203bis=0
dx204=0
dy204=0
dx204bis=0
dy204bis=0
dx205=0
dy205=0
dx205bis=0
dy205bis=0
dx206=0
dy206=0
dx206bis=0
dy206bis=0
dx207=0
dy207=0
dx207bis=0
dy207bis=0
dx208=0
dy208=0
dx208bis=0
dy208bis=0
dx209=0
dy209=0
dx209bis=0
dy209bis=0
dx210=0
dy210=0
dx210bis=0
dy210bis=0
dx211=0
dy211=0
dx211bis=0
dy211bis=0
dx212=0
dy212=0
dx212bis=0
dy212bis=0
dx213=0
dy213=0
dx213bis=0
dy213bis=0
dx214=0
dy214=0
dx214bis=0
dy214bis=0
dx215=0
dy215=0
dx215bis=0
dy215bis=0
dx216=0
dy216=0
dx216bis=0
dy216bis=0
dx217=0
dy217=0
dx217bis=0
dy217bis=0
dx218=0
dy218=0
dx218bis=0
dy218bis=0
dx219=0
dy219=0
dx219bis=0
dy219bis=0
dx220=0
dy220=0
dx220bis=0
dy220bis=0
dx221=0
dy221=0
dx221bis=0
dy221bis=0
dx222=0
dy222=0
dx222bis=0
dy222bis=0
dx223=0
dy223=0
dx223bis=0
dy223bis=0
dx224=0
dy224=0
dx224bis=0
dy224bis=0
dx225=0
dy225=0
dx225bis=0
dy225bis=0
dx226=0
dy226=0
dx226bis=0
dy226bis=0
dx227=0
dy227=0
dx227bis=0
dy227bis=0
dx228=0
dy228=0
dx228bis=0
dy228bis=0
dx229=0
dy229=0
dx229bis=0
dy229bis=0
dx230=0
dy230=0
dx230bis=0
dy230bis=0
dx231=0
dy231=0
dx231bis=0
dy231bis=0
dx232=0
dy232=0
dx232bis=0
dy232bis=0
dx233=0
dy233=0
dx233bis=0
dy233bis=0
dx234=0
dy234=0
dx234bis=0
dy234bis=0
dx235=0
dy235=0
dx235bis=0
dy235bis=0
dx236=0
dy236=0
dx236bis=0
dy236bis=0
dx237=0
dy237=0
dx237bis=0
dy237bis=0
dx238=0
dy238=0
dx238bis=0
dy238bis=0
dx239=0
dy239=0
dx239bis=0
dy239bis=0
dx240=0
dy240=0
dx240bis=0
dy240bis=0
dx241=0
dy241=0
dx241bis=0
dy241bis=0
dx242=0
dy242=0
dx242bis=0
dy242bis=0
dx243=0
dy243=0
dx243bis=0
dy243bis=0
dx244=0
dy244=0
dx244bis=0
dy244bis=0
dx245=0
dy245=0
dx245bis=0
dy245bis=0
dx246=0
dy246=0
dx246bis=0
dy246bis=0
dx247=0
dy247=0
dx247bis=0
dy247bis=0
dx248=0
dy248=0
dx248bis=0
dy248bis=0
dx249=0
dy249=0
dx249bis=0
dy249bis=0
dx250=0
dy250=0
dx250bis=0
dy250bis=0
dx251=0
dy251=0
dx251bis=0
dy251bis=0
dx252=0
dy252=0
dx252bis=0
dy252bis=0
dx253=0
dy253=0
dx253bis=0
dy253bis=0
dx254=0
dy254=0
dx254bis=0
dy254bis=0
dx255=0
dy255=0
dx255bis=0
dy255bis=0
dx256=0
dy256=0
dx256bis=0
dy256bis=0
dx257=0
dy257=0
dx257bis=0
dy257bis=0
dx258=0
dy258=0
dx258bis=0
dy258bis=0
dx259=0
dy259=0
dx259bis=0
dy259bis=0
dx260=0
dy260=0
dx260bis=0
dy260bis=0
dx261=0
dy261=0
dx261bis=0
dy261bis=0
dx262=0
dy262=0
dx262bis=0
dy262bis=0
dx263=0
dy263=0
dx263bis=0
dy263bis=0
dx264=0
dy264=0
dx264bis=0
dy264bis=0
dx265=0
dy265=0
dx265bis=0
dy265bis=0
dx266=0
dy266=0
dx266bis=0
dy266bis=0
dx267=0
dy267=0
dx267bis=0
dy267bis=0
dx268=0
dy268=0
dx268bis=0
dy268bis=0
dx269=0
dy269=0
dx269bis=0
dy269bis=0
dx270=0
dy270=0
dx270bis=0
dy270bis=0
dx271=0
dy271=0
dx271bis=0
dy271bis=0
dx272=0
dy272=0
dx272bis=0
dy272bis=0
dx273=0
dy273=0
dx273bis=0
dy273bis=0
dx274=0
dy274=0
dx274bis=0
dy274bis=0
dx275=0
dy275=0
dx275bis=0
dy275bis=0
dx276=0
dy276=0
dx276bis=0
dy276bis=0
dx277=0
dy277=0
dx277bis=0
dy277bis=0
dx278=0
dy278=0
dx278bis=0
dy278bis=0
dx279=0
dy279=0
dx279bis=0
dy279bis=0
dx280=0
dy280=0
dx280bis=0
dy280bis=0
dx281=0
dy281=0
dx281bis=0
dy281bis=0
dx282=0
dy282=0
dx282bis=0
dy282bis=0
dx283=0
dy283=0
dx283bis=0
dy283bis=0
dx284=0
dy284=0
dx284bis=0
dy284bis=0
dx285=0
dy285=0
dx285bis=0
dy285bis=0
dx286=0
dy286=0
dx286bis=0
dy286bis=0
dx287=0
dy287=0
dx287bis=0
dy287bis=0
dx288=0
dy288=0
dx288bis=0
dy288bis=0
dx289=0
dy289=0
dx289bis=0
dy289bis=0
dx290=0
dy290=0
dx290bis=0
dy290bis=0
dx291=0
dy291=0
dx291bis=0
dy291bis=0
dx292=0
dy292=0
dx292bis=0
dy292bis=0
dx293=0
dy293=0
dx293bis=0
dy293bis=0
dx294=0
dy294=0
dx294bis=0
dy294bis=0
dx295=0
dy295=0
dx295bis=0
dy295bis=0
dx296=0
dy296=0
dx296bis=0
dy296bis=0
dx297=0
dy297=0
dx297bis=0
dy297bis=0
dx298=0
dy298=0
dx298bis=0
dy298bis=0
dx299=0
dy299=0
dx299bis=0
dy299bis=0
dx300=0
dy300=0
dx300bis=0
dy300bis=0
dx301=0
dy301=0
dx301bis=0
dy301bis=0
dx302=0
dy302=0
dx302bis=0
dy302bis=0
dx303=0
dy303=0
dx303bis=0
dy303bis=0
dx304=0
dy304=0
dx304bis=0
dy304bis=0
dx305=0
dy305=0
dx305bis=0
dy305bis=0
dx306=0
dy306=0
dx306bis=0
dy306bis=0
dx307=0
dy307=0
dx307bis=0
dy307bis=0
dx308=0
dy308=0
dx308bis=0
dy308bis=0
dx309=0
dy309=0
dx309bis=0
dy309bis=0
dx310=0
dy310=0
dx310bis=0
dy310bis=0
dx311=0
dy311=0
dx311bis=0
dy311bis=0
dx312=0
dy312=0
dx312bis=0
dy312bis=0
dx313=0
dy313=0
dx313bis=0
dy313bis=0
dx314=0
dy314=0
dx314bis=0
dy314bis=0
dx315=0
dy315=0
dx315bis=0
dy315bis=0
dx316=0
dy316=0
dx316bis=0
dy316bis=0
dx317=0
dy317=0
dx317bis=0
dy317bis=0
dx318=0
dy318=0
dx318bis=0
dy318bis=0
dx319=0
dy319=0
dx319bis=0
dy319bis=0
dx320=0
dy320=0
dx320bis=0
dy320bis=0
dx321=0
dy321=0
dx321bis=0
dy321bis=0
dx322=0
dy322=0
dx322bis=0
dy322bis=0
dx323=0
dy323=0
dx323bis=0
dy323bis=0
dx324=0
dy324=0
dx324bis=0
dy324bis=0
dx325=0
dy325=0
dx325bis=0
dy325bis=0
dx326=0
dy326=0
dx326bis=0
dy326bis=0
dx327=0
dy327=0
dx327bis=0
dy327bis=0
dx328=0
dy328=0
dx328bis=0
dy328bis=0
dx329=0
dy329=0
dx329bis=0
dy329bis=0
dx330=0
dy330=0
dx330bis=0
dy330bis=0
dx331=0
dy331=0
dx331bis=0
dy331bis=0
dx332=0
dy332=0
dx332bis=0
dy332bis=0
dx333=0
dy333=0
dx333bis=0
dy333bis=0
dx334=0
dy334=0
dx334bis=0
dy334bis=0
dx335=0
dy335=0
dx335bis=0
dy335bis=0
dx336=0
dy336=0
dx336bis=0
dy336bis=0
dx337=0
dy337=0
dx337bis=0
dy337bis=0
dx338=0
dy338=0
dx338bis=0
dy338bis=0
dx339=0
dy339=0
dx339bis=0
dy339bis=0
dx340=0
dy340=0
dx340bis=0
dy340bis=0
dx341=0
dy341=0
dx341bis=0
dy341bis=0
dx342=0
dy342=0
dx342bis=0
dy342bis=0
dx343=0
dy343=0
dx343bis=0
dy343bis=0
dx344=0
dy344=0
dx344bis=0
dy344bis=0
dx345=0
dy345=0
dx345bis=0
dy345bis=0
dx346=0
dy346=0
dx346bis=0
dy346bis=0
dx347=0
dy347=0
dx347bis=0
dy347bis=0
dx348=0
dy348=0
dx348bis=0
dy348bis=0
dx349=0
dy349=0
dx349bis=0
dy349bis=0
dx350=0
dy350=0
dx350bis=0
dy350bis=0
dx351=0
dy351=0
dx351bis=0
dy351bis=0
dx352=0
dy352=0
dx352bis=0
dy352bis=0
dx353=0
dy353=0
dx353bis=0
dy353bis=0
dx354=0
dy354=0
dx354bis=0
dy354bis=0
dx355=0
dy355=0
dx355bis=0
dy355bis=0
dx356=0
dy356=0
dx356bis=0
dy356bis=0
dx357=0
dy357=0
dx357bis=0
dy357bis=0
dx358=0
dy358=0
dx358bis=0
dy358bis=0
dx359=0
dy359=0
dx359bis=0
dy359bis=0
dx360=0
dy360=0
dx360bis=0
dy360bis=0
dx361=0
dy361=0
dx361bis=0
dy361bis=0
dx362=0
dy362=0
dx362bis=0
dy362bis=0
dx363=0
dy363=0
dx363bis=0
dy363bis=0
dx364=0
dy364=0
dx364bis=0
dy364bis=0
dx365=0
dy365=0
dx365bis=0
dy365bis=0
dx366=0
dy366=0
dx366bis=0
dy366bis=0
dx367=0
dy367=0
dx367bis=0
dy367bis=0
dx368=0
dy368=0
dx368bis=0
dy368bis=0
dx369=0
dy369=0
dx369bis=0
dy369bis=0
dx370=0
dy370=0
dx370bis=0
dy370bis=0
dx371=0
dy371=0
dx371bis=0
dy371bis=0
dx372=0
dy372=0
dx372bis=0
dy372bis=0
dx373=0
dy373=0
dx373bis=0
dy373bis=0
dx374=0
dy374=0
dx374bis=0
dy374bis=0
dx375=0
dy375=0
dx375bis=0
dy375bis=0
dx376=0
dy376=0
dx376bis=0
dy376bis=0
dx377=0
dy377=0
dx377bis=0
dy377bis=0
dx378=0
dy378=0
dx378bis=0
dy378bis=0
dx379=0
dy379=0
dx379bis=0
dy379bis=0
dx380=0
dy380=0
dx380bis=0
dy380bis=0
dx381=0
dy381=0
dx381bis=0
dy381bis=0
dx382=0
dy382=0
dx382bis=0
dy382bis=0
dx383=0
dy383=0
dx383bis=0
dy383bis=0
dx384=0
dy384=0
dx384bis=0
dy384bis=0
dx385=0
dy385=0
dx385bis=0
dy385bis=0
dx386=0
dy386=0
dx386bis=0
dy386bis=0
dx387=0
dy387=0
dx387bis=0
dy387bis=0
dx388=0
dy388=0
dx388bis=0
dy388bis=0
dx389=0
dy389=0
dx389bis=0
dy389bis=0
dx390=0
dy390=0
dx390bis=0
dy390bis=0
dx391=0
dy391=0
dx391bis=0
dy391bis=0
dx392=0
dy392=0
dx392bis=0
dy392bis=0
dx393=0
dy393=0
dx393bis=0
dy393bis=0
dx394=0
dy394=0
dx394bis=0
dy394bis=0
dx395=0
dy395=0
dx395bis=0
dy395bis=0
dx396=0
dy396=0
dx396bis=0
dy396bis=0
dx397=0
dy397=0
dx397bis=0
dy397bis=0
dx398=0
dy398=0
dx398bis=0
dy398bis=0
dx399=0
dy399=0
dx399bis=0
dy399bis=0
dx400=0
dy400=0
dx400bis=0
dy400bis=0
dx401=0
dy401=0
dx401bis=0
dy401bis=0
dx402=0
dy402=0
dx402bis=0
dy402bis=0
dx403=0
dy403=0
dx403bis=0
dy403bis=0
dx404=0
dy404=0
dx404bis=0
dy404bis=0
dx405=0
dy405=0
dx405bis=0
dy405bis=0
dx406=0
dy406=0
dx406bis=0
dy406bis=0
dx407=0
dy407=0
dx407bis=0
dy407bis=0
dx408=0
dy408=0
dx408bis=0
dy408bis=0
dx409=0
dy409=0
dx409bis=0
dy409bis=0
dx410=0
dy410=0
dx410bis=0
dy410bis=0
dx411=0
dy411=0
dx411bis=0
dy411bis=0
dx412=0
dy412=0
dx412bis=0
dy412bis=0
dx413=0
dy413=0
dx413bis=0
dy413bis=0
dx414=0
dy414=0
dx414bis=0
dy414bis=0
dx415=0
dy415=0
dx415bis=0
dy415bis=0
dx416=0
dy416=0
dx416bis=0
dy416bis=0
dx417=0
dy417=0
dx417bis=0
dy417bis=0
dx418=0
dy418=0
dx418bis=0
dy418bis=0
dx419=0
dy419=0
dx419bis=0
dy419bis=0
dx420=0
dy420=0
dx420bis=0
dy420bis=0
dx421=0
dy421=0
dx421bis=0
dy421bis=0
dx422=0
dy422=0
dx422bis=0
dy422bis=0
dx423=0
dy423=0
dx423bis=0
dy423bis=0
dx424=0
dy424=0
dx424bis=0
dy424bis=0
dx425=0
dy425=0
dx425bis=0
dy425bis=0
dx426=0
dy426=0
dx426bis=0
dy426bis=0
dx427=0
dy427=0
dx427bis=0
dy427bis=0
dx428=0
dy428=0
dx428bis=0
dy428bis=0
dx429=0
dy429=0
dx429bis=0
dy429bis=0
dx430=0
dy430=0
dx430bis=0
dy430bis=0
dx431=0
dy431=0
dx431bis=0
dy431bis=0
dx432=0
dy432=0
dx432bis=0
dy432bis=0
dx433=0
dy433=0
dx433bis=0
dy433bis=0
dx434=0
dy434=0
dx434bis=0
dy434bis=0
dx435=0
dy435=0
dx435bis=0
dy435bis=0
dx436=0
dy436=0
dx436bis=0
dy436bis=0
dx437=0
dy437=0
dx437bis=0
dy437bis=0
dx438=0
dy438=0
dx438bis=0
dy438bis=0
dx439=0
dy439=0
dx439bis=0
dy439bis=0
dx440=0
dy440=0
dx440bis=0
dy440bis=0
dx441=0
dy441=0
dx441bis=0
dy441bis=0
dx442=0
dy442=0
dx442bis=0
dy442bis=0
dx443=0
dy443=0
dx443bis=0
dy443bis=0
dx444=0
dy444=0
dx444bis=0
dy444bis=0
dx445=0
dy445=0
dx445bis=0
dy445bis=0
dx446=0
dy446=0
dx446bis=0
dy446bis=0
dx447=0
dy447=0
dx447bis=0
dy447bis=0
dx448=0
dy448=0
dx448bis=0
dy448bis=0
dx449=0
dy449=0
dx449bis=0
dy449bis=0
dx450=0
dy450=0
dx450bis=0
dy450bis=0
dx451=0
dy451=0
dx451bis=0
dy451bis=0
dx452=0
dy452=0
dx452bis=0
dy452bis=0
dx453=0
dy453=0
dx453bis=0
dy453bis=0
dx454=0
dy454=0
dx454bis=0
dy454bis=0
dx455=0
dy455=0
dx455bis=0
dy455bis=0
dx456=0
dy456=0
dx456bis=0
dy456bis=0
dx457=0
dy457=0
dx457bis=0
dy457bis=0
dx458=0
dy458=0
dx458bis=0
dy458bis=0
dx459=0
dy459=0
dx459bis=0
dy459bis=0
dx460=0
dy460=0
dx460bis=0
dy460bis=0
dx461=0
dy461=0
dx461bis=0
dy461bis=0
dx462=0
dy462=0
dx462bis=0
dy462bis=0
dx463=0
dy463=0
dx463bis=0
dy463bis=0
dx464=0
dy464=0
dx464bis=0
dy464bis=0
dx465=0
dy465=0
dx465bis=0
dy465bis=0
dx466=0
dy466=0
dx466bis=0
dy466bis=0
dx467=0
dy467=0
dx467bis=0
dy467bis=0
dx468=0
dy468=0
dx468bis=0
dy468bis=0
dx469=0
dy469=0
dx469bis=0
dy469bis=0
dx470=0
dy470=0
dx470bis=0
dy470bis=0
dx471=0
dy471=0
dx471bis=0
dy471bis=0
dx472=0
dy472=0
dx472bis=0
dy472bis=0
dx473=0
dy473=0
dx473bis=0
dy473bis=0
dx474=0
dy474=0
dx474bis=0
dy474bis=0
dx475=0
dy475=0
dx475bis=0
dy475bis=0
dx476=0
dy476=0
dx476bis=0
dy476bis=0
dx477=0
dy477=0
dx477bis=0
dy477bis=0
dx478=0
dy478=0
dx478bis=0
dy478bis=0
dx479=0
dy479=0
dx479bis=0
dy479bis=0
dx480=0
dy480=0
dx480bis=0
dy480bis=0
dx481=0
dy481=0
dx481bis=0
dy481bis=0
dx482=0
dy482=0
dx482bis=0
dy482bis=0
dx483=0
dy483=0
dx483bis=0
dy483bis=0
dx484=0
dy484=0
dx484bis=0
dy484bis=0
player=0

#les variables de la pomme
a=45
b=45
c=45
d=45



#variable qui permet d'eviter qu'une condition se lance en boucle
dlol=0
isz=0
music=1
music1=0

#les différentes coordonées possibles de la pomme
def coordoneex():
    global i
    T=[15,45,75,105,135,165,195,225,255,285,315,345,375,405,435,465,495,525,555,585,615,645]
    i=random.randint(0,21)
    return T[i]

def coordoneey():
    global j
    T=[15,45,75,105,135,165,195,225,255,285,315,345,375,405,435,465,495,525,555,585,615,645]
    j=random.randint(0,21)
    return T[j]

#le damier en arriére plan.
def damier():
    for y in range(0,655,60):
        for x in range(0,655,60):
            monCanevas.create_rectangle(x,y,x+30,y+30,fill="green",outline="green")
            monCanevas.create_rectangle(x+30,y+30,x+60,y+60,fill="green",outline="green")

#definition de l'évenement "le joueur appuis sur une touche" ici zqsd.
def z (event):
    global dx,dy,player
    touche=event.keysym

    if touche =="z" or touche=="Z":
        dx=0
        dy=-30
        player=1
    elif touche =="d" or touche=="D":
        dx=30
        dy=0
        player=1
    elif touche =="s" or touche=="S":
        dx=0
        dy=30
        player=1
    elif touche =="q" or touche=="Q":
        dx=-30
        dy=0
        player=1

#l'animation qui va définir le mouvement du serpent
def animation():

        #les variables
        global dx,dlol,dy,dx1,dy1,dx1bis,dy1bis,dy2bis,dx2bis,dd1,dd2,dx2,dy2,dy3bis,dx3bis,dx3,dy3,dx4bis,dy4bis,dx4,dy4,dx5bis,dy5bis,dx5,dy5,dx6bis,dy6bis,dx6,dy6,dx7bis,dy7bis,dx7,dy7,dx8bis,dy8bis,dx8,dy8,dx9bis,dy9bis,dx9,dy9,dx10bis,dy10bis,dx10,dy10,dx11bis,dy11bis,dx11,dy11,dx12bis,dy12bis,dx12,dy12,dx13bis,dy13bis,dx13,dy13,dx14bis,dy14bis,dx14,dy14,dx15bis,dy15bis,dx15,dy15,dx16bis,dy16bis,dx16,dy16,dx17bis,dy17bis,dx17,dy17,dx18bis,dy18bis,dx18,dy18,dx19bis,dy19bis,dx19,dy19,dx20bis,dy20bis,dx20,dy20,dx21bis,dy21bis,dx21,dy21,dx22bis,dy22bis,dx22,dy22,dx23bis,dy23bis,dx23,dy24,dx24bis,dy24bis,dx24,dy24,dx25bis,dy25bis,dx25,dy25,dx26bis,dy26bis,dx26,dy26,dx27bis,dy27bis,dx27,dy27,a,b,c,d,isz,player,music,music1

        global dx28bis,dy28bis,dx28,dy28,dx29bis,dy29bis,dx29,dy29,dx30bis,dy30bis,dx30,dy30,dx31bis,dy31bis,dx31,dy31
        global dx32bis,dy32bis,dx32,dy32,dx33bis,dy33bis,dx33,dy33,dx34bis,dy34bis,dx34,dy34,dx35bis,dy35bis,dx35,dy35
        global dx36bis,dy36bis,dx36,dy36,dx37bis,dy37bis,dx37,dy37,dx38bis,dy38bis,dx38,dy38,dx39bis,dy39bis,dx39,dy39
        global dx40bis,dy40bis,dx40,dy40,dx41bis,dy41bis,dx41,dy41,dx42bis,dy42bis,dx42,dy42,dx43bis,dy43bis,dx43,dy43
        global dx44bis,dy44bis,dx44,dy44,dx45bis,dy45bis,dx45,dy45,dx46bis,dy46bis,dx46,dy46,dx47bis,dy47bis,dx47,dy47
        global dx48bis,dy48bis,dx48,dy48,dx49bis,dy49bis,dx49,dy49,dx50bis,dy50bis,dx50,dy50,dx51bis,dy51bis,dx51,dy51
        global dx52bis,dy52bis,dx52,dy52,dx53bis,dy53bis,dx53,dy53,dx54bis,dy54bis,dx54,dy54,dx55bis,dy55bis,dx55,dy55
        global dx56bis,dy56bis,dx56,dy56,dx57bis,dy57bis,dx57,dy57,dx58bis,dy58bis,dx58,dy58,dx59bis,dy59bis,dx59,dy59
        global dx60bis,dy60bis,dx60,dy60,dx61bis,dy61bis,dx61,dy61,dx62bis,dy62bis,dx62,dy62,dx63bis,dy63bis,dx63,dy63
        global dx64bis,dy64bis,dx64,dy64,dx65bis,dy65bis,dx65,dy65,dx66bis,dy66bis,dx66,dy66,dx67bis,dy67bis,dx67,dy67
        global dx68bis,dy68bis,dx68,dy68,dx69bis,dy69bis,dx69,dy69,dx70bis,dy70bis,dx70,dy70,dx71bis,dy71bis,dx71,dy71
        global dx72bis,dy72bis,dx72,dy72,dx73bis,dy73bis,dx73,dy73,dx74bis,dy74bis,dx74,dy74,dx75bis,dy75bis,dx75,dy75
        global dx76bis,dy76bis,dx76,dy76,dx77bis,dy77bis,dx77,dy77,dx78bis,dy78bis,dx78,dy78,dx79bis,dy79bis,dx79,dy79
        global dx80bis,dy80bis,dx80,dy80,dx81bis,dy81bis,dx81,dy81,dx82bis,dy82bis,dx82,dy82,dx83bis,dy83bis,dx83,dy83
        global dx84bis,dy84bis,dx84,dy84,dx85bis,dy85bis,dx85,dy85,dx86bis,dy86bis,dx86,dy86,dx87bis,dy87bis,dx87,dy87
        global dx88bis,dy88bis,dx88,dy88,dx89bis,dy89bis,dx89,dy89,dx90bis,dy90bis,dx90,dy90,dx91bis,dy91bis,dx91,dy91
        global dx92bis,dy92bis,dx92,dy92,dx93bis,dy93bis,dx93,dy93,dx94bis,dy94bis,dx94,dy94,dx95bis,dy95bis,dx95,dy95
        global dx96bis,dy96bis,dx96,dy96,dx97bis,dy97bis,dx97,dy97,dx98bis,dy98bis,dx98,dy98,dx99bis,dy99bis,dx99,dy99
        global dx100bis,dy100bis,dx100,dy100,dx101bis,dy101bis,dx101,dy101,dx102bis,dy102bis,dx102,dy102,dx103bis,dy103bis,dx103,dy103
        global dx104bis,dy104bis,dx104,dy104,dx105bis,dy105bis,dx105,dy105,dx106bis,dy106bis,dx106,dy106,dx107bis,dy107bis,dx107,dy107
        global dx108bis,dy108bis,dx108,dy108,dx109bis,dy109bis,dx109,dy109,dx110bis,dy110bis,dx110,dy110,dx111bis,dy111bis,dx111,dy111
        global dx112bis,dy112bis,dx112,dy112,dx113bis,dy113bis,dx113,dy113,dx114bis,dy114bis,dx114,dy114,dx115bis,dy115bis,dx115,dy115
        global dx116bis,dy116bis,dx116,dy116,dx117bis,dy117bis,dx117,dy117,dx118bis,dy118bis,dx118,dy118,dx119bis,dy119bis,dx119,dy119
        global dx120bis,dy120bis,dx120,dy120,dx121bis,dy121bis,dx121,dy121,dx122bis,dy122bis,dx122,dy122,dx123bis,dy123bis,dx123,dy123
        global dx124bis,dy124bis,dx124,dy124,dx125bis,dy125bis,dx125,dy125,dx126bis,dy126bis,dx126,dy126,dx127bis,dy127bis,dx127,dy127
        global dx128bis,dy128bis,dx128,dy128,dx129bis,dy129bis,dx129,dy129,dx130bis,dy130bis,dx130,dy130,dx131bis,dy131bis,dx131,dy131
        global dx132bis,dy132bis,dx132,dy132,dx133bis,dy133bis,dx133,dy133,dx134bis,dy134bis,dx134,dy134,dx135bis,dy135bis,dx135,dy135
        global dx136bis,dy136bis,dx136,dy136,dx137bis,dy137bis,dx137,dy137,dx138bis,dy138bis,dx138,dy138,dx139bis,dy139bis,dx139,dy139
        global dx140bis,dy140bis,dx140,dy140,dx141bis,dy141bis,dx141,dy141,dx142bis,dy142bis,dx142,dy142,dx143bis,dy143bis,dx143,dy143
        global dx144bis,dy144bis,dx144,dy144,dx145bis,dy145bis,dx145,dy145,dx146bis,dy146bis,dx146,dy146,dx147bis,dy147bis,dx147,dy147
        global dx148bis,dy148bis,dx148,dy148,dx149bis,dy149bis,dx149,dy149,dx150bis,dy150bis,dx150,dy150,dx151bis,dy151bis,dx151,dy151
        global dx152bis,dy152bis,dx152,dy152,dx153bis,dy153bis,dx153,dy153,dx154bis,dy154bis,dx154,dy154,dx155bis,dy155bis,dx155,dy155
        global dx156bis,dy156bis,dx156,dy156,dx157bis,dy157bis,dx157,dy157,dx158bis,dy158bis,dx158,dy158,dx159bis,dy159bis,dx159,dy159
        global dx160bis,dy160bis,dx160,dy160,dx161bis,dy161bis,dx161,dy161,dx162bis,dy162bis,dx162,dy162,dx163bis,dy163bis,dx163,dy163
        global dx164bis,dy164bis,dx164,dy164,dx165bis,dy165bis,dx165,dy165,dx166bis,dy166bis,dx166,dy166,dx167bis,dy167bis,dx167,dy167
        global dx168bis,dy168bis,dx168,dy168,dx169bis,dy169bis,dx169,dy169,dx170bis,dy170bis,dx170,dy170,dx171bis,dy171bis,dx171,dy171
        global dx172bis,dy172bis,dx172,dy172,dx173bis,dy173bis,dx173,dy173,dx174bis,dy174bis,dx174,dy174,dx175bis,dy175bis,dx175,dy175
        global dx176bis,dy176bis,dx176,dy176,dx177bis,dy177bis,dx177,dy177,dx178bis,dy178bis,dx178,dy178,dx179bis,dy179bis,dx179,dy179
        global dx180bis,dy180bis,dx180,dy180,dx181bis,dy181bis,dx181,dy181,dx182bis,dy182bis,dx182,dy182,dx183bis,dy183bis,dx183,dy183
        global dx184bis,dy184bis,dx184,dy184,dx185bis,dy185bis,dx185,dy185,dx186bis,dy186bis,dx186,dy186,dx187bis,dy187bis,dx187,dy187
        global dx188bis,dy188bis,dx188,dy188,dx189bis,dy189bis,dx189,dy189,dx190bis,dy190bis,dx190,dy190,dx191bis,dy191bis,dx191,dy191
        global dx192bis,dy192bis,dx192,dy192,dx193bis,dy193bis,dx193,dy193,dx194bis,dy194bis,dx194,dy194,dx195bis,dy195bis,dx195,dy195
        global dx196bis,dy196bis,dx196,dy196,dx197bis,dy197bis,dx197,dy197,dx198bis,dy198bis,dx198,dy198,dx199bis,dy199bis,dx199,dy199
        global dx200bis,dy200bis,dx200,dy200,dx201bis,dy201bis,dx201,dy201,dx202bis,dy202bis,dx202,dy202,dx203bis,dy203bis,dx203,dy203
        global dx204bis,dy204bis,dx204,dy204,dx205bis,dy205bis,dx205,dy205,dx206bis,dy206bis,dx206,dy206,dx207bis,dy207bis,dx207,dy207
        global dx208bis,dy208bis,dx208,dy208,dx209bis,dy209bis,dx209,dy209,dx210bis,dy210bis,dx210,dy210,dx211bis,dy211bis,dx211,dy211
        global dx212bis,dy212bis,dx212,dy212,dx213bis,dy213bis,dx213,dy213,dx214bis,dy214bis,dx214,dy214,dx215bis,dy215bis,dx215,dy215
        global dx216bis,dy216bis,dx216,dy216,dx217bis,dy217bis,dx217,dy217,dx218bis,dy218bis,dx218,dy218,dx219bis,dy219bis,dx219,dy219
        global dx220bis,dy220bis,dx220,dy220,dx221bis,dy221bis,dx221,dy221,dx222bis,dy222bis,dx222,dy222,dx223bis,dy223bis,dx223,dy223
        global dx224bis,dy224bis,dx224,dy224,dx225bis,dy225bis,dx225,dy225,dx226bis,dy226bis,dx226,dy226,dx227bis,dy227bis,dx227,dy227
        global dx228bis,dy228bis,dx228,dy228,dx229bis,dy229bis,dx229,dy229,dx230bis,dy230bis,dx230,dy230,dx231bis,dy231bis,dx231,dy231
        global dx232bis,dy232bis,dx232,dy232,dx233bis,dy233bis,dx233,dy233,dx234bis,dy234bis,dx234,dy234,dx235bis,dy235bis,dx235,dy235
        global dx236bis,dy236bis,dx236,dy236,dx237bis,dy237bis,dx237,dy237,dx238bis,dy238bis,dx238,dy238,dx239bis,dy239bis,dx239,dy239
        global dx240bis,dy240bis,dx240,dy240,dx241bis,dy241bis,dx241,dy241,dx242bis,dy242bis,dx242,dy242,dx243bis,dy243bis,dx243,dy243
        global dx244bis,dy244bis,dx244,dy244,dx245bis,dy245bis,dx245,dy245,dx246bis,dy246bis,dx246,dy246,dx247bis,dy247bis,dx247,dy247
        global dx248bis,dy248bis,dx248,dy248,dx249bis,dy249bis,dx249,dy249,dx250bis,dy250bis,dx250,dy250,dx251bis,dy251bis,dx251,dy251
        global dx252bis,dy252bis,dx252,dy252,dx253bis,dy253bis,dx253,dy253,dx254bis,dy254bis,dx254,dy254,dx255bis,dy255bis,dx255,dy255
        global dx256bis,dy256bis,dx256,dy256,dx257bis,dy257bis,dx257,dy257,dx258bis,dy258bis,dx258,dy258,dx259bis,dy259bis,dx259,dy259
        global dx260bis,dy260bis,dx260,dy260,dx261bis,dy261bis,dx261,dy261,dx262bis,dy262bis,dx262,dy262,dx263bis,dy263bis,dx263,dy263
        global dx264bis,dy264bis,dx264,dy264,dx265bis,dy265bis,dx265,dy265,dx266bis,dy266bis,dx266,dy266,dx267bis,dy267bis,dx267,dy267
        global dx268bis,dy268bis,dx268,dy268,dx269bis,dy269bis,dx269,dy269,dx270bis,dy270bis,dx270,dy270,dx271bis,dy271bis,dx271,dy271
        global dx272bis,dy272bis,dx272,dy272,dx273bis,dy273bis,dx273,dy273,dx274bis,dy274bis,dx274,dy274,dx275bis,dy275bis,dx275,dy275
        global dx276bis,dy276bis,dx276,dy276,dx277bis,dy277bis,dx277,dy277,dx278bis,dy278bis,dx278,dy278,dx279bis,dy279bis,dx279,dy279
        global dx280bis,dy280bis,dx280,dy280,dx281bis,dy281bis,dx281,dy281,dx282bis,dy282bis,dx282,dy282,dx283bis,dy283bis,dx283,dy283
        global dx284bis,dy284bis,dx284,dy284,dx285bis,dy285bis,dx285,dy285,dx286bis,dy286bis,dx286,dy286,dx287bis,dy287bis,dx287,dy287
        global dx288bis,dy288bis,dx288,dy288,dx289bis,dy289bis,dx289,dy289,dx290bis,dy290bis,dx290,dy290,dx291bis,dy291bis,dx291,dy291
        global dx292bis,dy292bis,dx292,dy292,dx293bis,dy293bis,dx293,dy293,dx294bis,dy294bis,dx294,dy294,dx295bis,dy295bis,dx295,dy295
        global dx296bis,dy296bis,dx296,dy296,dx297bis,dy297bis,dx297,dy297,dx298bis,dy298bis,dx298,dy298,dx299bis,dy299bis,dx299,dy299
        global dx300bis,dy300bis,dx300,dy300,dx301bis,dy301bis,dx301,dy301,dx302bis,dy302bis,dx302,dy302,dx303bis,dy303bis,dx303,dy303
        global dx304bis,dy304bis,dx304,dy304,dx305bis,dy305bis,dx305,dy305,dx306bis,dy306bis,dx306,dy306,dx307bis,dy307bis,dx307,dy307
        global dx308bis,dy308bis,dx308,dy308,dx309bis,dy309bis,dx309,dy309,dx310bis,dy310bis,dx310,dy310,dx311bis,dy311bis,dx311,dy311
        global dx312bis,dy312bis,dx312,dy312,dx313bis,dy313bis,dx313,dy313,dx314bis,dy314bis,dx314,dy314,dx315bis,dy315bis,dx315,dy315
        global dx316bis,dy316bis,dx316,dy316,dx317bis,dy317bis,dx317,dy317,dx318bis,dy318bis,dx318,dy318,dx319bis,dy319bis,dx319,dy319
        global dx320bis,dy320bis,dx320,dy320,dx321bis,dy321bis,dx321,dy321,dx322bis,dy322bis,dx322,dy322,dx323bis,dy323bis,dx323,dy323
        global dx324bis,dy324bis,dx324,dy324,dx325bis,dy325bis,dx325,dy325,dx326bis,dy326bis,dx326,dy326,dx327bis,dy327bis,dx327,dy327
        global dx328bis,dy328bis,dx328,dy328,dx329bis,dy329bis,dx329,dy329,dx330bis,dy330bis,dx330,dy330,dx331bis,dy331bis,dx331,dy331
        global dx332bis,dy332bis,dx332,dy332,dx333bis,dy333bis,dx333,dy333,dx334bis,dy334bis,dx334,dy334,dx335bis,dy335bis,dx335,dy335
        global dx336bis,dy336bis,dx336,dy336,dx337bis,dy337bis,dx337,dy337,dx338bis,dy338bis,dx338,dy338,dx339bis,dy339bis,dx339,dy339
        global dx340bis,dy340bis,dx340,dy340,dx341bis,dy341bis,dx341,dy341,dx342bis,dy342bis,dx342,dy342,dx343bis,dy343bis,dx343,dy343
        global dx344bis,dy344bis,dx344,dy344,dx345bis,dy345bis,dx345,dy345,dx346bis,dy346bis,dx346,dy346,dx347bis,dy347bis,dx347,dy347
        global dx348bis,dy348bis,dx348,dy348,dx349bis,dy349bis,dx349,dy349,dx350bis,dy350bis,dx350,dy350,dx351bis,dy351bis,dx351,dy351
        global dx352bis,dy352bis,dx352,dy352,dx353bis,dy353bis,dx353,dy353,dx354bis,dy354bis,dx354,dy354,dx355bis,dy355bis,dx355,dy355
        global dx356bis,dy356bis,dx356,dy356,dx357bis,dy357bis,dx357,dy357,dx358bis,dy358bis,dx358,dy358,dx359bis,dy359bis,dx359,dy359
        global dx360bis,dy360bis,dx360,dy360,dx361bis,dy361bis,dx361,dy361,dx362bis,dy362bis,dx362,dy362,dx363bis,dy363bis,dx363,dy363
        global dx364bis,dy364bis,dx364,dy364,dx365bis,dy365bis,dx365,dy365,dx366bis,dy366bis,dx366,dy366,dx367bis,dy367bis,dx367,dy367
        global dx368bis,dy368bis,dx368,dy368,dx369bis,dy369bis,dx369,dy369,dx370bis,dy370bis,dx370,dy370,dx371bis,dy371bis,dx371,dy371
        global dx372bis,dy372bis,dx372,dy372,dx373bis,dy373bis,dx373,dy373,dx374bis,dy374bis,dx374,dy374,dx375bis,dy375bis,dx375,dy375
        global dx376bis,dy376bis,dx376,dy376,dx377bis,dy377bis,dx377,dy377,dx378bis,dy378bis,dx378,dy378,dx379bis,dy379bis,dx379,dy379
        global dx380bis,dy380bis,dx380,dy380,dx381bis,dy381bis,dx381,dy381,dx382bis,dy382bis,dx382,dy382,dx383bis,dy383bis,dx383,dy383
        global dx384bis,dy384bis,dx384,dy384,dx385bis,dy385bis,dx385,dy385,dx386bis,dy386bis,dx386,dy386,dx387bis,dy387bis,dx387,dy387
        global dx388bis,dy388bis,dx388,dy388,dx389bis,dy389bis,dx389,dy389,dx390bis,dy390bis,dx390,dy390,dx391bis,dy391bis,dx391,dy391
        global dx392bis,dy392bis,dx392,dy392,dx393bis,dy393bis,dx393,dy393,dx394bis,dy394bis,dx394,dy394,dx395bis,dy395bis,dx395,dy395
        global dx396bis,dy396bis,dx396,dy396,dx397bis,dy397bis,dx397,dy397,dx398bis,dy398bis,dx398,dy398,dx399bis,dy399bis,dx399,dy399
        global dx400bis,dy400bis,dx400,dy400,dx401bis,dy401bis,dx401,dy401,dx402bis,dy402bis,dx402,dy402,dx403bis,dy403bis,dx403,dy403
        global dx404bis,dy404bis,dx404,dy404,dx405bis,dy405bis,dx405,dy405,dx406bis,dy406bis,dx406,dy406,dx407bis,dy407bis,dx407,dy407
        global dx408bis,dy408bis,dx408,dy408,dx409bis,dy409bis,dx409,dy409,dx410bis,dy410bis,dx410,dy410,dx411bis,dy411bis,dx411,dy411
        global dx412bis,dy412bis,dx412,dy412,dx413bis,dy413bis,dx413,dy413,dx414bis,dy414bis,dx414,dy414,dx415bis,dy415bis,dx415,dy415
        global dx416bis,dy416bis,dx416,dy416,dx417bis,dy417bis,dx417,dy417,dx418bis,dy418bis,dx418,dy418,dx419bis,dy419bis,dx419,dy419
        global dx420bis,dy420bis,dx420,dy420,dx421bis,dy421bis,dx421,dy421,dx422bis,dy422bis,dx422,dy422,dx423bis,dy423bis,dx423,dy423
        global dx424bis,dy424bis,dx424,dy424,dx425bis,dy425bis,dx425,dy425,dx426bis,dy426bis,dx426,dy426,dx427bis,dy427bis,dx427,dy427
        global dx428bis,dy428bis,dx428,dy428,dx429bis,dy429bis,dx429,dy429,dx430bis,dy430bis,dx430,dy430,dx431bis,dy431bis,dx431,dy431
        global dx432bis,dy432bis,dx432,dy432,dx433bis,dy433bis,dx433,dy433,dx434bis,dy434bis,dx434,dy434,dx435bis,dy435bis,dx435,dy435
        global dx436bis,dy436bis,dx436,dy436,dx437bis,dy437bis,dx437,dy437,dx438bis,dy438bis,dx438,dy438,dx439bis,dy439bis,dx439,dy439
        global dx440bis,dy440bis,dx440,dy440,dx441bis,dy441bis,dx441,dy441,dx442bis,dy442bis,dx442,dy442,dx443bis,dy443bis,dx443,dy443
        global dx444bis,dy444bis,dx444,dy444,dx445bis,dy445bis,dx445,dy445,dx446bis,dy446bis,dx446,dy446,dx447bis,dy447bis,dx447,dy447
        global dx448bis,dy448bis,dx448,dy448,dx449bis,dy449bis,dx449,dy449,dx450bis,dy450bis,dx450,dy450,dx451bis,dy451bis,dx451,dy451
        global dx452bis,dy452bis,dx452,dy452,dx453bis,dy453bis,dx453,dy453,dx454bis,dy454bis,dx454,dy454,dx455bis,dy455bis,dx455,dy455
        global dx456bis,dy456bis,dx456,dy456,dx457bis,dy457bis,dx457,dy457,dx458bis,dy458bis,dx458,dy458,dx459bis,dy459bis,dx459,dy459
        global dx460bis,dy460bis,dx460,dy460,dx461bis,dy461bis,dx461,dy461,dx462bis,dy462bis,dx462,dy462,dx463bis,dy463bis,dx463,dy463
        global dx464bis,dy464bis,dx464,dy464,dx465bis,dy465bis,dx465,dy465,dx466bis,dy466bis,dx466,dy466,dx467bis,dy467bis,dx467,dy467
        global dx468bis,dy468bis,dx468,dy468,dx469bis,dy469bis,dx469,dy469,dx470bis,dy470bis,dx470,dy470,dx471bis,dy471bis,dx471,dy471
        global dx472bis,dy472bis,dx472,dy472,dx473bis,dy473bis,dx473,dy473,dx474bis,dy474bis,dx474,dy474,dx475bis,dy475bis,dx475,dy475
        global dx476bis,dy476bis,dx476,dy476,dx477bis,dy477bis,dx477,dy477,dx478bis,dy478bis,dx478,dy478,dx479bis,dy479bis,dx479,dy479
        global dx480bis,dy480bis,dx480,dy480,dx481bis,dy481bis,dx481,dy481,dx482bis,dy482bis,dx482,dy482,dx483bis,dy483bis,dx483,dy483
        global dx484bis,dy484bis,dx484,dy484

        #la musique s'arette si le joueur perd
        if music1==0 :
            music1=1
            megalovania()
        if music==0 and music1==1 :
            music1=2
            pygame.mixer.stop()
            lost()

        #le programme assignie ici les variavles du cube de devant a la
        #derniére animation (les variables bis) aux variables du cube actuel
        #permet de transmettre la position de cube en cube)
        dx1=dx1bis
        dy1=dy1bis
        dy1bis=dy
        dx1bis=dx
        dx2=dx2bis
        dy2=dy2bis
        dx3=dx3bis
        dy3=dy3bis
        dy4=dy4bis
        dx4=dx4bis
        dy5=dy5bis
        dx5=dx5bis
        dy6=dy6bis
        dx6=dx6bis
        dy7=dy7bis
        dx7=dx7bis
        dy8=dy8bis
        dx8=dx8bis
        dy9=dy9bis
        dx9=dx9bis
        dy10=dy10bis
        dx10=dx10bis
        dy11=dy11bis
        dx11=dx11bis
        dy12=dy12bis
        dx12=dx12bis
        dy13=dy13bis
        dx13=dx13bis
        dy14=dy14bis
        dx14=dx14bis
        dy15=dy15bis
        dx15=dx15bis
        dy16=dy16bis
        dx16=dx16bis
        dy17=dy17bis
        dx17=dx17bis
        dy18=dy18bis
        dx18=dx18bis
        dy19=dy19bis
        dx19=dx19bis
        dy20=dy20bis
        dx20=dx20bis
        dy21=dy21bis
        dx21=dx21bis
        dy22=dy22bis
        dx22=dx22bis
        dy23=dy23bis
        dx23=dx23bis
        dy24=dy24bis
        dx24=dx24bis
        dy25=dy25bis
        dy25=dy25bis
        dx25=dx25bis
        dy26=dy26bis
        dx26=dx26bis
        dy27=dy27bis
        dx27=dx27bis
        dy28=dy28bis
        dx28=dx28bis
        dy29=dy29bis
        dx29=dx29bis
        dy30=dy30bis
        dx30=dx30bis
        dy31=dy31bis
        dx31=dx31bis
        dy32=dy32bis
        dx32=dx32bis
        dy33=dy33bis
        dx33=dx33bis
        dy34=dy34bis
        dx34=dx34bis
        dy35=dy35bis
        dx35=dx35bis
        dy36=dy36bis
        dx36=dx36bis
        dy37=dy37bis
        dx37=dx37bis
        dy38=dy38bis
        dx38=dx38bis
        dy39=dy39bis
        dx39=dx39bis
        dy40=dy40bis
        dx40=dx40bis
        dy41=dy41bis
        dx41=dx41bis
        dy42=dy42bis
        dx42=dx42bis
        dy43=dy43bis
        dx43=dx43bis
        dy44=dy44bis
        dx44=dx44bis
        dy45=dy45bis
        dx45=dx45bis
        dy46=dy46bis
        dx46=dx46bis
        dy47=dy47bis
        dx47=dx47bis
        dy48=dy48bis
        dx48=dx48bis
        dy49=dy49bis
        dx49=dx49bis
        dy50=dy50bis
        dx50=dx50bis
        dy51=dy51bis
        dx51=dx51bis
        dy52=dy52bis
        dx52=dx52bis
        dy53=dy53bis
        dx53=dx53bis
        dy54=dy54bis
        dx54=dx54bis
        dy55=dy55bis
        dx55=dx55bis
        dy56=dy56bis
        dx56=dx56bis
        dy57=dy57bis
        dx57=dx57bis
        dy58=dy58bis
        dx58=dx58bis
        dy59=dy59bis
        dx59=dx59bis
        dy60=dy60bis
        dx60=dx60bis
        dy61=dy61bis
        dx61=dx61bis
        dy62=dy62bis
        dx62=dx62bis
        dy63=dy63bis
        dx63=dx63bis
        dy64=dy64bis
        dx64=dx64bis
        dy65=dy65bis
        dx65=dx65bis
        dy66=dy66bis
        dx66=dx66bis
        dy67=dy67bis
        dx67=dx67bis
        dy68=dy68bis
        dx68=dx68bis
        dy69=dy69bis
        dx69=dx69bis
        dy70=dy70bis
        dx70=dx70bis
        dy71=dy71bis
        dx71=dx71bis
        dy72=dy72bis
        dx72=dx72bis
        dy73=dy73bis
        dx73=dx73bis
        dy74=dy74bis
        dx74=dx74bis
        dy75=dy75bis
        dx75=dx75bis
        dy76=dy76bis
        dx76=dx76bis
        dy77=dy77bis
        dx77=dx77bis
        dy78=dy78bis
        dx78=dx78bis
        dy79=dy79bis
        dx79=dx79bis
        dy80=dy80bis
        dx80=dx80bis
        dy81=dy81bis
        dx81=dx81bis
        dy82=dy82bis
        dx82=dx82bis
        dy83=dy83bis
        dx83=dx83bis
        dy84=dy84bis
        dx84=dx84bis
        dy85=dy85bis
        dx85=dx85bis
        dy86=dy86bis
        dx86=dx86bis
        dy87=dy87bis
        dx87=dx87bis
        dy88=dy88bis
        dx88=dx88bis
        dy89=dy89bis
        dx89=dx89bis
        dy90=dy90bis
        dx90=dx90bis
        dy91=dy91bis
        dx91=dx91bis
        dy92=dy92bis
        dx92=dx92bis
        dy93=dy93bis
        dx93=dx93bis
        dy94=dy94bis
        dx94=dx94bis
        dy95=dy95bis
        dx95=dx95bis
        dy96=dy96bis
        dx96=dx96bis
        dy97=dy97bis
        dx97=dx97bis
        dy98=dy98bis
        dx98=dx98bis
        dy99=dy99bis
        dx99=dx99bis
        dy100=dy100bis
        dx100=dx100bis
        dy101=dy101bis
        dx101=dx101bis
        dy102=dy102bis
        dx102=dx102bis
        dy103=dy103bis
        dx103=dx103bis
        dy104=dy104bis
        dx104=dx104bis
        dy105=dy105bis
        dx105=dx105bis
        dy106=dy106bis
        dx106=dx106bis
        dy107=dy107bis
        dx107=dx107bis
        dy108=dy108bis
        dx108=dx108bis
        dy109=dy109bis
        dx109=dx109bis
        dy110=dy110bis
        dx110=dx110bis
        dy111=dy111bis
        dx111=dx111bis
        dy112=dy112bis
        dx112=dx112bis
        dy113=dy113bis
        dx113=dx113bis
        dy114=dy114bis
        dx114=dx114bis
        dy115=dy115bis
        dx115=dx115bis
        dy116=dy116bis
        dx116=dx116bis
        dy117=dy117bis
        dx117=dx117bis
        dy118=dy118bis
        dx118=dx118bis
        dy119=dy119bis
        dx119=dx119bis
        dy120=dy120bis
        dx120=dx120bis
        dy121=dy121bis
        dx121=dx121bis
        dy122=dy122bis
        dx122=dx122bis
        dy123=dy123bis
        dx123=dx123bis
        dy124=dy124bis
        dx124=dx124bis
        dy125=dy125bis
        dx125=dx125bis
        dy126=dy126bis
        dx126=dx126bis
        dy127=dy127bis
        dx127=dx127bis
        dy128=dy128bis
        dx128=dx128bis
        dy129=dy129bis
        dx129=dx129bis
        dy130=dy130bis
        dx130=dx130bis
        dy131=dy131bis
        dx131=dx131bis
        dy132=dy132bis
        dx132=dx132bis
        dy133=dy133bis
        dx133=dx133bis
        dy134=dy134bis
        dx134=dx134bis
        dy135=dy135bis
        dx135=dx135bis
        dy136=dy136bis
        dx136=dx136bis
        dy137=dy137bis
        dx137=dx137bis
        dy138=dy138bis
        dx138=dx138bis
        dy139=dy139bis
        dx139=dx139bis
        dy140=dy140bis
        dx140=dx140bis
        dy141=dy141bis
        dx141=dx141bis
        dy142=dy142bis
        dx142=dx142bis
        dy143=dy143bis
        dx143=dx143bis
        dy144=dy144bis
        dx144=dx144bis
        dy145=dy145bis
        dx145=dx145bis
        dy146=dy146bis
        dx146=dx146bis
        dy147=dy147bis
        dx147=dx147bis
        dy148=dy148bis
        dx148=dx148bis
        dy149=dy149bis
        dx149=dx149bis
        dy150=dy150bis
        dx150=dx150bis
        dy151=dy151bis
        dx151=dx151bis
        dy152=dy152bis
        dx152=dx152bis
        dy153=dy153bis
        dx153=dx153bis
        dy154=dy154bis
        dx154=dx154bis
        dy155=dy155bis
        dx155=dx155bis
        dy156=dy156bis
        dx156=dx156bis
        dy157=dy157bis
        dx157=dx157bis
        dy158=dy158bis
        dx158=dx158bis
        dy159=dy159bis
        dx159=dx159bis
        dy160=dy160bis
        dx160=dx160bis
        dy161=dy161bis
        dx161=dx161bis
        dy162=dy162bis
        dx162=dx162bis
        dy163=dy163bis
        dx163=dx163bis
        dy164=dy164bis
        dx164=dx164bis
        dy165=dy165bis
        dx165=dx165bis
        dy166=dy166bis
        dx166=dx166bis
        dy167=dy167bis
        dx167=dx167bis
        dy168=dy168bis
        dx168=dx168bis
        dy169=dy169bis
        dx169=dx169bis
        dy170=dy170bis
        dx170=dx170bis
        dy171=dy171bis
        dx171=dx171bis
        dy172=dy172bis
        dx172=dx172bis
        dy173=dy173bis
        dx173=dx173bis
        dy174=dy174bis
        dx174=dx174bis
        dy175=dy175bis
        dx175=dx175bis
        dy176=dy176bis
        dx176=dx176bis
        dy177=dy177bis
        dx177=dx177bis
        dy178=dy178bis
        dx178=dx178bis
        dy179=dy179bis
        dx179=dx179bis
        dy180=dy180bis
        dx180=dx180bis
        dy181=dy181bis
        dx181=dx181bis
        dy182=dy182bis
        dx182=dx182bis
        dy183=dy183bis
        dx183=dx183bis
        dy184=dy184bis
        dx184=dx184bis
        dy185=dy185bis
        dx185=dx185bis
        dy186=dy186bis
        dx186=dx186bis
        dy187=dy187bis
        dx187=dx187bis
        dy188=dy188bis
        dx188=dx188bis
        dy189=dy189bis
        dx189=dx189bis
        dy190=dy190bis
        dx190=dx190bis
        dy191=dy191bis
        dx191=dx191bis
        dy192=dy192bis
        dx192=dx192bis
        dy193=dy193bis
        dx193=dx193bis
        dy194=dy194bis
        dx194=dx194bis
        dy195=dy195bis
        dx195=dx195bis
        dy196=dy196bis
        dx196=dx196bis
        dy197=dy197bis
        dx197=dx197bis
        dy198=dy198bis
        dx198=dx198bis
        dy199=dy199bis
        dx199=dx199bis
        dy200=dy200bis
        dx200=dx200bis
        dy201=dy201bis
        dx201=dx201bis
        dy202=dy202bis
        dx202=dx202bis
        dy203=dy203bis
        dx203=dx203bis
        dy204=dy204bis
        dx204=dx204bis
        dy205=dy205bis
        dx205=dx205bis
        dy206=dy206bis
        dx206=dx206bis
        dy207=dy207bis
        dx207=dx207bis
        dy208=dy208bis
        dx208=dx208bis
        dy209=dy209bis
        dx209=dx209bis
        dy210=dy210bis
        dx210=dx210bis
        dy211=dy211bis
        dx211=dx211bis
        dy212=dy212bis
        dx212=dx212bis
        dy213=dy213bis
        dx213=dx213bis
        dy214=dy214bis
        dx214=dx214bis
        dy215=dy215bis
        dx215=dx215bis
        dy216=dy216bis
        dx216=dx216bis
        dy217=dy217bis
        dx217=dx217bis
        dy218=dy218bis
        dx218=dx218bis
        dy219=dy219bis
        dx219=dx219bis
        dy220=dy220bis
        dx220=dx220bis
        dy221=dy221bis
        dx221=dx221bis
        dy222=dy222bis
        dx222=dx222bis
        dy223=dy223bis
        dx223=dx223bis
        dy224=dy224bis
        dx224=dx224bis
        dy225=dy225bis
        dx225=dx225bis
        dy226=dy226bis
        dx226=dx226bis
        dy227=dy227bis
        dx227=dx227bis
        dy228=dy228bis
        dx228=dx228bis
        dy229=dy229bis
        dx229=dx229bis
        dy230=dy230bis
        dx230=dx230bis
        dy231=dy231bis
        dx231=dx231bis
        dy232=dy232bis
        dx232=dx232bis
        dy233=dy233bis
        dx233=dx233bis
        dy234=dy234bis
        dx234=dx234bis
        dy235=dy235bis
        dx235=dx235bis
        dy236=dy236bis
        dx236=dx236bis
        dy237=dy237bis
        dx237=dx237bis
        dy238=dy238bis
        dx238=dx238bis
        dy239=dy239bis
        dx239=dx239bis
        dy240=dy240bis
        dx240=dx240bis
        dy241=dy241bis
        dx241=dx241bis
        dy242=dy242bis
        dx242=dx242bis
        dy243=dy243bis
        dx243=dx243bis
        dy244=dy244bis
        dx244=dx244bis
        dy245=dy245bis
        dx245=dx245bis
        dy246=dy246bis
        dx246=dx246bis
        dy247=dy247bis
        dx247=dx247bis
        dy248=dy248bis
        dx248=dx248bis
        dy249=dy249bis
        dx249=dx249bis
        dy250=dy250bis
        dx250=dx250bis
        dy251=dy251bis
        dx251=dx251bis
        dy252=dy252bis
        dx252=dx252bis
        dy253=dy253bis
        dx253=dx253bis
        dy254=dy254bis
        dx254=dx254bis
        dy255=dy255bis
        dx255=dx255bis
        dy256=dy256bis
        dx256=dx256bis
        dy257=dy257bis
        dx257=dx257bis
        dy258=dy258bis
        dx258=dx258bis
        dy259=dy259bis
        dx259=dx259bis
        dy260=dy260bis
        dx260=dx260bis
        dy261=dy261bis
        dx261=dx261bis
        dy262=dy262bis
        dx262=dx262bis
        dy263=dy263bis
        dx263=dx263bis
        dy264=dy264bis
        dx264=dx264bis
        dy265=dy265bis
        dx265=dx265bis
        dy266=dy266bis
        dx266=dx266bis
        dy267=dy267bis
        dx267=dx267bis
        dy268=dy268bis
        dx268=dx268bis
        dy269=dy269bis
        dx269=dx269bis
        dy270=dy270bis
        dx270=dx270bis
        dy271=dy271bis
        dx271=dx271bis
        dy272=dy272bis
        dx272=dx272bis
        dy273=dy273bis
        dx273=dx273bis
        dy274=dy274bis
        dx274=dx274bis
        dy275=dy275bis
        dx275=dx275bis
        dy276=dy276bis
        dx276=dx276bis
        dy277=dy277bis
        dx277=dx277bis
        dy278=dy278bis
        dx278=dx278bis
        dy279=dy279bis
        dx279=dx279bis
        dy280=dy280bis
        dx280=dx280bis
        dy281=dy281bis
        dx281=dx281bis
        dy282=dy282bis
        dx282=dx282bis
        dy283=dy283bis
        dx283=dx283bis
        dy284=dy284bis
        dx284=dx284bis
        dy285=dy285bis
        dx285=dx285bis
        dy286=dy286bis
        dx286=dx286bis
        dy287=dy287bis
        dx287=dx287bis
        dy288=dy288bis
        dx288=dx288bis
        dy289=dy289bis
        dx289=dx289bis
        dy290=dy290bis
        dx290=dx290bis
        dy291=dy291bis
        dx291=dx291bis
        dy292=dy292bis
        dx292=dx292bis
        dy293=dy293bis
        dx293=dx293bis
        dy294=dy294bis
        dx294=dx294bis
        dy295=dy295bis
        dx295=dx295bis
        dy296=dy296bis
        dx296=dx296bis
        dy297=dy297bis
        dx297=dx297bis
        dy298=dy298bis
        dx298=dx298bis
        dy299=dy299bis
        dx299=dx299bis
        dy300=dy300bis
        dx300=dx300bis
        dy301=dy301bis
        dx301=dx301bis
        dy302=dy302bis
        dx302=dx302bis
        dy303=dy303bis
        dx303=dx303bis
        dy304=dy304bis
        dx304=dx304bis
        dy305=dy305bis
        dx305=dx305bis
        dy306=dy306bis
        dx306=dx306bis
        dy307=dy307bis
        dx307=dx307bis
        dy308=dy308bis
        dx308=dx308bis
        dy309=dy309bis
        dx309=dx309bis
        dy310=dy310bis
        dx310=dx310bis
        dy311=dy311bis
        dx311=dx311bis
        dy312=dy312bis
        dx312=dx312bis
        dy313=dy313bis
        dx313=dx313bis
        dy314=dy314bis
        dx314=dx314bis
        dy315=dy315bis
        dx315=dx315bis
        dy316=dy316bis
        dx316=dx316bis
        dy317=dy317bis
        dx317=dx317bis
        dy318=dy318bis
        dx318=dx318bis
        dy319=dy319bis
        dx319=dx319bis
        dy320=dy320bis
        dx320=dx320bis
        dy321=dy321bis
        dx321=dx321bis
        dy322=dy322bis
        dx322=dx322bis
        dy323=dy323bis
        dx323=dx323bis
        dy324=dy324bis
        dx324=dx324bis
        dy325=dy325bis
        dx325=dx325bis
        dy326=dy326bis
        dx326=dx326bis
        dy327=dy327bis
        dx327=dx327bis
        dy328=dy328bis
        dx328=dx328bis
        dy329=dy329bis
        dx329=dx329bis
        dy330=dy330bis
        dx330=dx330bis
        dy331=dy331bis
        dx331=dx331bis
        dy332=dy332bis
        dx332=dx332bis
        dy333=dy333bis
        dx333=dx333bis
        dy334=dy334bis
        dx334=dx334bis
        dy335=dy335bis
        dx335=dx335bis
        dy336=dy336bis
        dx336=dx336bis
        dy337=dy337bis
        dx337=dx337bis
        dy338=dy338bis
        dx338=dx338bis
        dy339=dy339bis
        dx339=dx339bis
        dy340=dy340bis
        dx340=dx340bis
        dy341=dy341bis
        dx341=dx341bis
        dy342=dy342bis
        dx342=dx342bis
        dy343=dy343bis
        dx343=dx343bis
        dy344=dy344bis
        dx344=dx344bis
        dy345=dy345bis
        dx345=dx345bis
        dy346=dy346bis
        dx346=dx346bis
        dy347=dy347bis
        dx347=dx347bis
        dy348=dy348bis
        dx348=dx348bis
        dy349=dy349bis
        dx349=dx349bis
        dy350=dy350bis
        dx350=dx350bis
        dy351=dy351bis
        dx351=dx351bis
        dy352=dy352bis
        dx352=dx352bis
        dy353=dy353bis
        dx353=dx353bis
        dy354=dy354bis
        dx354=dx354bis
        dy355=dy355bis
        dx355=dx355bis
        dy356=dy356bis
        dx356=dx356bis
        dy357=dy357bis
        dx357=dx357bis
        dy358=dy358bis
        dx358=dx358bis
        dy359=dy359bis
        dx359=dx359bis
        dy360=dy360bis
        dx360=dx360bis
        dy361=dy361bis
        dx361=dx361bis
        dy362=dy362bis
        dx362=dx362bis
        dy363=dy363bis
        dx363=dx363bis
        dy364=dy364bis
        dx364=dx364bis
        dy365=dy365bis
        dx365=dx365bis
        dy366=dy366bis
        dx366=dx366bis
        dy367=dy367bis
        dx367=dx367bis
        dy368=dy368bis
        dx368=dx368bis
        dy369=dy369bis
        dx369=dx369bis
        dy370=dy370bis
        dx370=dx370bis
        dy371=dy371bis
        dx371=dx371bis
        dy372=dy372bis
        dx372=dx372bis
        dy373=dy373bis
        dx373=dx373bis
        dy374=dy374bis
        dx374=dx374bis
        dy375=dy375bis
        dx375=dx375bis
        dy376=dy376bis
        dx376=dx376bis
        dy377=dy377bis
        dx377=dx377bis
        dy378=dy378bis
        dx378=dx378bis
        dy379=dy379bis
        dx379=dx379bis
        dy380=dy380bis
        dx380=dx380bis
        dy381=dy381bis
        dx381=dx381bis
        dy382=dy382bis
        dx382=dx382bis
        dy383=dy383bis
        dx383=dx383bis
        dy384=dy384bis
        dx384=dx384bis
        dy385=dy385bis
        dx385=dx385bis
        dy386=dy386bis
        dx386=dx386bis
        dy387=dy387bis
        dx387=dx387bis
        dy388=dy388bis
        dx388=dx388bis
        dy389=dy389bis
        dx389=dx389bis
        dy390=dy390bis
        dx390=dx390bis
        dy391=dy391bis
        dx391=dx391bis
        dy392=dy392bis
        dx392=dx392bis
        dy393=dy393bis
        dx393=dx393bis
        dy394=dy394bis
        dx394=dx394bis
        dy395=dy395bis
        dx395=dx395bis
        dy396=dy396bis
        dx396=dx396bis
        dy397=dy397bis
        dx397=dx397bis
        dy398=dy398bis
        dx398=dx398bis
        dy399=dy399bis
        dx399=dx399bis
        dy400=dy400bis
        dx400=dx400bis
        dy401=dy401bis
        dx401=dx401bis
        dy402=dy402bis
        dx402=dx402bis
        dy403=dy403bis
        dx403=dx403bis
        dy404=dy404bis
        dx404=dx404bis
        dy405=dy405bis
        dx405=dx405bis
        dy406=dy406bis
        dx406=dx406bis
        dy407=dy407bis
        dx407=dx407bis
        dy408=dy408bis
        dx408=dx408bis
        dy409=dy409bis
        dx409=dx409bis
        dy410=dy410bis
        dx410=dx410bis
        dy411=dy411bis
        dx411=dx411bis
        dy412=dy412bis
        dx412=dx412bis
        dy413=dy413bis
        dx413=dx413bis
        dy414=dy414bis
        dx414=dx414bis
        dy415=dy415bis
        dx415=dx415bis
        dy416=dy416bis
        dx416=dx416bis
        dy417=dy417bis
        dx417=dx417bis
        dy418=dy418bis
        dx418=dx418bis
        dy419=dy419bis
        dx419=dx419bis
        dy420=dy420bis
        dx420=dx420bis
        dy421=dy421bis
        dx421=dx421bis
        dy422=dy422bis
        dx422=dx422bis
        dy423=dy423bis
        dx423=dx423bis
        dy424=dy424bis
        dx424=dx424bis
        dy425=dy425bis
        dx425=dx425bis
        dy426=dy426bis
        dx426=dx426bis
        dy427=dy427bis
        dx427=dx427bis
        dy428=dy428bis
        dx428=dx428bis
        dy429=dy429bis
        dx429=dx429bis
        dy430=dy430bis
        dx430=dx430bis
        dy431=dy431bis
        dx431=dx431bis
        dy432=dy432bis
        dx432=dx432bis
        dy433=dy433bis
        dx433=dx433bis
        dy434=dy434bis
        dx434=dx434bis
        dy435=dy435bis
        dx435=dx435bis
        dy436=dy436bis
        dx436=dx436bis
        dy437=dy437bis
        dx437=dx437bis
        dy438=dy438bis
        dx438=dx438bis
        dy439=dy439bis
        dx439=dx439bis
        dy440=dy440bis
        dx440=dx440bis
        dy441=dy441bis
        dx441=dx441bis
        dy442=dy442bis
        dx442=dx442bis
        dy443=dy443bis
        dx443=dx443bis
        dy444=dy444bis
        dx444=dx444bis
        dy445=dy445bis
        dx445=dx445bis
        dy446=dy446bis
        dx446=dx446bis
        dy447=dy447bis
        dx447=dx447bis
        dy448=dy448bis
        dx448=dx448bis
        dy449=dy449bis
        dx449=dx449bis
        dy450=dy450bis
        dx450=dx450bis
        dy451=dy451bis
        dx451=dx451bis
        dy452=dy452bis
        dx452=dx452bis
        dy453=dy453bis
        dx453=dx453bis
        dy454=dy454bis
        dx454=dx454bis
        dy455=dy455bis
        dx455=dx455bis
        dy456=dy456bis
        dx456=dx456bis
        dy457=dy457bis
        dx457=dx457bis
        dy458=dy458bis
        dx458=dx458bis
        dy459=dy459bis
        dx459=dx459bis
        dy460=dy460bis
        dx460=dx460bis
        dy461=dy461bis
        dx461=dx461bis
        dy462=dy462bis
        dx462=dx462bis
        dy463=dy463bis
        dx463=dx463bis
        dy464=dy464bis
        dx464=dx464bis
        dy465=dy465bis
        dx465=dx465bis
        dy466=dy466bis
        dx466=dx466bis
        dy467=dy467bis
        dx467=dx467bis
        dy468=dy468bis
        dx468=dx468bis
        dy469=dy469bis
        dx469=dx469bis
        dy470=dy470bis
        dx470=dx470bis
        dy471=dy471bis
        dx471=dx471bis
        dy472=dy472bis
        dx472=dx472bis
        dy473=dy473bis
        dx473=dx473bis
        dy474=dy474bis
        dx474=dx474bis
        dy475=dy475bis
        dx475=dx475bis
        dy476=dy476bis
        dx476=dx476bis
        dy477=dy477bis
        dx477=dx477bis
        dy478=dy478bis
        dx478=dx478bis
        dy479=dy479bis
        dx479=dx479bis
        dy480=dy480bis
        dx480=dx480bis
        dy481=dy481bis
        dx481=dx481bis
        dy482=dy482bis
        dx482=dx482bis
        dy483=dy483bis
        dx483=dx483bis
        dy484=dy484bis
        dx484=dx484bis
        if player==1 :
            isz=isz+1

        #definition du mouvement de la tete
        coordonneesBalle=monCanevas.bbox(balle)
        x=coordonneesBalle[0]
        y=coordonneesBalle[1]

        #aplications de la position des différents carrés a des variables
        coordonneesBalle2=monCanevas.bbox(balle2)
        x2=coordonneesBalle2[0]
        y2=coordonneesBalle2[1]

        coordonneesBalle3=monCanevas.bbox(balle3)
        x3=coordonneesBalle3[0]
        y3=coordonneesBalle3[1]

        coordonneesBalle4=monCanevas.bbox(balle4)
        x4=coordonneesBalle4[0]
        y4=coordonneesBalle4[1]

        coordonneesBalle5=monCanevas.bbox(balle5)
        x5=coordonneesBalle5[0]
        y5=coordonneesBalle5[1]

        coordonneesBalle6=monCanevas.bbox(balle6)
        x6=coordonneesBalle6[0]
        y6=coordonneesBalle6[1]

        coordonneesBalle7=monCanevas.bbox(balle7)
        x7=coordonneesBalle7[0]
        y7=coordonneesBalle7[1]

        coordonneesBalle8=monCanevas.bbox(balle8)
        x8=coordonneesBalle8[0]
        y8=coordonneesBalle8[1]

        coordonneesBalle9=monCanevas.bbox(balle9)
        x9=coordonneesBalle9[0]
        y9=coordonneesBalle9[1]

        coordonneesBalle10=monCanevas.bbox(balle10)
        x10=coordonneesBalle10[0]
        y10=coordonneesBalle10[1]

        coordonneesBalle11=monCanevas.bbox(balle11)
        x11=coordonneesBalle11[0]
        y11=coordonneesBalle11[1]

        coordonneesBalle12=monCanevas.bbox(balle12)
        x12=coordonneesBalle12[0]
        y12=coordonneesBalle12[1]

        coordonneesBalle13=monCanevas.bbox(balle13)
        x13=coordonneesBalle13[0]
        y13=coordonneesBalle13[1]

        coordonneesBalle14=monCanevas.bbox(balle14)
        x14=coordonneesBalle14[0]
        y14=coordonneesBalle14[1]

        coordonneesBalle15=monCanevas.bbox(balle15)
        x15=coordonneesBalle15[0]
        y15=coordonneesBalle15[1]

        coordonneesBalle16=monCanevas.bbox(balle16)
        x16=coordonneesBalle16[0]
        y16=coordonneesBalle16[1]

        coordonneesBalle17=monCanevas.bbox(balle17)
        x17=coordonneesBalle17[0]
        y17=coordonneesBalle17[1]

        coordonneesBalle18=monCanevas.bbox(balle18)
        x18=coordonneesBalle18[0]
        y18=coordonneesBalle18[1]

        coordonneesBalle19=monCanevas.bbox(balle19)
        x19=coordonneesBalle19[0]
        y19=coordonneesBalle19[1]

        coordonneesBalle20=monCanevas.bbox(balle20)
        x20=coordonneesBalle20[0]
        y20=coordonneesBalle20[1]

        coordonneesBalle21=monCanevas.bbox(balle21)
        x21=coordonneesBalle21[0]
        y21=coordonneesBalle21[1]

        coordonneesBalle22=monCanevas.bbox(balle22)
        x22=coordonneesBalle22[0]
        y22=coordonneesBalle22[1]

        coordonneesBalle23=monCanevas.bbox(balle23)
        x23=coordonneesBalle23[0]
        y23=coordonneesBalle23[1]

        coordonneesBalle24=monCanevas.bbox(balle24)
        x24=coordonneesBalle24[0]
        y24=coordonneesBalle24[1]

        coordonneesBalle25=monCanevas.bbox(balle25)
        x25=coordonneesBalle25[0]
        y25=coordonneesBalle25[1]

        coordonneesBalle26=monCanevas.bbox(balle26)
        x26=coordonneesBalle26[0]
        y26=coordonneesBalle26[1]

        coordonneesBalle27=monCanevas.bbox(balle27)
        x27=coordonneesBalle27[0]
        y27=coordonneesBalle27[1]

        coordonneesBalle28=monCanevas.bbox(balle28)
        x28=coordonneesBalle28[0]
        y28=coordonneesBalle28[1]

        coordonneesBalle29=monCanevas.bbox(balle29)
        x29=coordonneesBalle29[0]
        y29=coordonneesBalle29[1]

        coordonneesBalle30=monCanevas.bbox(balle30)
        x30=coordonneesBalle30[0]
        y30=coordonneesBalle30[1]

        coordonneesBalle31=monCanevas.bbox(balle31)
        x31=coordonneesBalle31[0]
        y31=coordonneesBalle31[1]

        coordonneesBalle32=monCanevas.bbox(balle32)
        x32=coordonneesBalle32[0]
        y32=coordonneesBalle32[1]

        coordonneesBalle33=monCanevas.bbox(balle33)
        x33=coordonneesBalle33[0]
        y33=coordonneesBalle33[1]

        coordonneesBalle34=monCanevas.bbox(balle34)
        x34=coordonneesBalle34[0]
        y34=coordonneesBalle34[1]

        coordonneesBalle35=monCanevas.bbox(balle35)
        x35=coordonneesBalle35[0]
        y35=coordonneesBalle35[1]

        coordonneesBalle36=monCanevas.bbox(balle36)
        x36=coordonneesBalle36[0]
        y36=coordonneesBalle36[1]

        coordonneesBalle37=monCanevas.bbox(balle37)
        x37=coordonneesBalle37[0]
        y37=coordonneesBalle37[1]

        coordonneesBalle38=monCanevas.bbox(balle38)
        x38=coordonneesBalle38[0]
        y38=coordonneesBalle38[1]

        coordonneesBalle39=monCanevas.bbox(balle39)
        x39=coordonneesBalle39[0]
        y39=coordonneesBalle39[1]

        coordonneesBalle40=monCanevas.bbox(balle40)
        x40=coordonneesBalle40[0]
        y40=coordonneesBalle40[1]

        coordonneesBalle41=monCanevas.bbox(balle41)
        x41=coordonneesBalle41[0]
        y41=coordonneesBalle41[1]

        coordonneesBalle42=monCanevas.bbox(balle42)
        x42=coordonneesBalle42[0]
        y42=coordonneesBalle42[1]

        coordonneesBalle43=monCanevas.bbox(balle43)
        x43=coordonneesBalle43[0]
        y43=coordonneesBalle43[1]

        coordonneesBalle44=monCanevas.bbox(balle44)
        x44=coordonneesBalle44[0]
        y44=coordonneesBalle44[1]

        coordonneesBalle45=monCanevas.bbox(balle45)
        x45=coordonneesBalle45[0]
        y45=coordonneesBalle45[1]

        coordonneesBalle46=monCanevas.bbox(balle46)
        x46=coordonneesBalle46[0]
        y46=coordonneesBalle46[1]

        coordonneesBalle47=monCanevas.bbox(balle47)
        x47=coordonneesBalle47[0]
        y47=coordonneesBalle47[1]

        coordonneesBalle48=monCanevas.bbox(balle48)
        x48=coordonneesBalle48[0]
        y48=coordonneesBalle48[1]

        coordonneesBalle49=monCanevas.bbox(balle49)
        x49=coordonneesBalle49[0]
        y49=coordonneesBalle49[1]

        coordonneesBalle50=monCanevas.bbox(balle50)
        x50=coordonneesBalle50[0]
        y50=coordonneesBalle50[1]

        coordonneesBalle51=monCanevas.bbox(balle51)
        x51=coordonneesBalle51[0]
        y51=coordonneesBalle51[1]

        coordonneesBalle52=monCanevas.bbox(balle52)
        x52=coordonneesBalle52[0]
        y52=coordonneesBalle52[1]

        coordonneesBalle53=monCanevas.bbox(balle53)
        x53=coordonneesBalle53[0]
        y53=coordonneesBalle53[1]

        coordonneesBalle54=monCanevas.bbox(balle54)
        x54=coordonneesBalle54[0]
        y54=coordonneesBalle54[1]

        coordonneesBalle55=monCanevas.bbox(balle55)
        x55=coordonneesBalle55[0]
        y55=coordonneesBalle55[1]

        coordonneesBalle56=monCanevas.bbox(balle56)
        x56=coordonneesBalle56[0]
        y56=coordonneesBalle56[1]

        coordonneesBalle57=monCanevas.bbox(balle57)
        x57=coordonneesBalle57[0]
        y57=coordonneesBalle57[1]

        coordonneesBalle58=monCanevas.bbox(balle58)
        x58=coordonneesBalle58[0]
        y58=coordonneesBalle58[1]

        coordonneesBalle59=monCanevas.bbox(balle59)
        x59=coordonneesBalle59[0]
        y59=coordonneesBalle59[1]

        coordonneesBalle60=monCanevas.bbox(balle60)
        x60=coordonneesBalle60[0]
        y60=coordonneesBalle60[1]

        coordonneesBalle61=monCanevas.bbox(balle61)
        x61=coordonneesBalle61[0]
        y61=coordonneesBalle61[1]

        coordonneesBalle62=monCanevas.bbox(balle62)
        x62=coordonneesBalle62[0]
        y62=coordonneesBalle62[1]

        coordonneesBalle63=monCanevas.bbox(balle63)
        x63=coordonneesBalle63[0]
        y63=coordonneesBalle63[1]

        coordonneesBalle64=monCanevas.bbox(balle64)
        x64=coordonneesBalle64[0]
        y64=coordonneesBalle64[1]

        coordonneesBalle65=monCanevas.bbox(balle65)
        x65=coordonneesBalle65[0]
        y65=coordonneesBalle65[1]

        coordonneesBalle66=monCanevas.bbox(balle66)
        x66=coordonneesBalle66[0]
        y66=coordonneesBalle66[1]

        coordonneesBalle67=monCanevas.bbox(balle67)
        x67=coordonneesBalle67[0]
        y67=coordonneesBalle67[1]

        coordonneesBalle68=monCanevas.bbox(balle68)
        x68=coordonneesBalle68[0]
        y68=coordonneesBalle68[1]

        coordonneesBalle69=monCanevas.bbox(balle69)
        x69=coordonneesBalle69[0]
        y69=coordonneesBalle69[1]

        coordonneesBalle70=monCanevas.bbox(balle70)
        x70=coordonneesBalle70[0]
        y70=coordonneesBalle70[1]

        coordonneesBalle71=monCanevas.bbox(balle71)
        x71=coordonneesBalle71[0]
        y71=coordonneesBalle71[1]

        coordonneesBalle72=monCanevas.bbox(balle72)
        x72=coordonneesBalle72[0]
        y72=coordonneesBalle72[1]

        coordonneesBalle73=monCanevas.bbox(balle73)
        x73=coordonneesBalle73[0]
        y73=coordonneesBalle73[1]

        coordonneesBalle74=monCanevas.bbox(balle74)
        x74=coordonneesBalle74[0]
        y74=coordonneesBalle74[1]

        coordonneesBalle75=monCanevas.bbox(balle75)
        x75=coordonneesBalle75[0]
        y75=coordonneesBalle75[1]

        coordonneesBalle76=monCanevas.bbox(balle76)
        x76=coordonneesBalle76[0]
        y76=coordonneesBalle76[1]

        coordonneesBalle77=monCanevas.bbox(balle77)
        x77=coordonneesBalle77[0]
        y77=coordonneesBalle77[1]

        coordonneesBalle78=monCanevas.bbox(balle78)
        x78=coordonneesBalle78[0]
        y78=coordonneesBalle78[1]

        coordonneesBalle79=monCanevas.bbox(balle79)
        x79=coordonneesBalle79[0]
        y79=coordonneesBalle79[1]

        coordonneesBalle80=monCanevas.bbox(balle80)
        x80=coordonneesBalle80[0]
        y80=coordonneesBalle80[1]

        coordonneesBalle81=monCanevas.bbox(balle81)
        x81=coordonneesBalle81[0]
        y81=coordonneesBalle81[1]

        coordonneesBalle82=monCanevas.bbox(balle82)
        x82=coordonneesBalle82[0]
        y82=coordonneesBalle82[1]

        coordonneesBalle83=monCanevas.bbox(balle83)
        x83=coordonneesBalle83[0]
        y83=coordonneesBalle83[1]

        coordonneesBalle84=monCanevas.bbox(balle84)
        x84=coordonneesBalle84[0]
        y84=coordonneesBalle84[1]

        coordonneesBalle85=monCanevas.bbox(balle85)
        x85=coordonneesBalle85[0]
        y85=coordonneesBalle85[1]

        coordonneesBalle86=monCanevas.bbox(balle86)
        x86=coordonneesBalle86[0]
        y86=coordonneesBalle86[1]

        coordonneesBalle87=monCanevas.bbox(balle87)
        x87=coordonneesBalle87[0]
        y87=coordonneesBalle87[1]

        coordonneesBalle88=monCanevas.bbox(balle88)
        x88=coordonneesBalle88[0]
        y88=coordonneesBalle88[1]

        coordonneesBalle89=monCanevas.bbox(balle89)
        x89=coordonneesBalle89[0]
        y89=coordonneesBalle89[1]

        coordonneesBalle90=monCanevas.bbox(balle90)
        x90=coordonneesBalle90[0]
        y90=coordonneesBalle90[1]

        coordonneesBalle91=monCanevas.bbox(balle91)
        x91=coordonneesBalle91[0]
        y91=coordonneesBalle91[1]

        coordonneesBalle92=monCanevas.bbox(balle92)
        x92=coordonneesBalle92[0]
        y92=coordonneesBalle92[1]

        coordonneesBalle93=monCanevas.bbox(balle93)
        x93=coordonneesBalle93[0]
        y93=coordonneesBalle93[1]

        coordonneesBalle94=monCanevas.bbox(balle94)
        x94=coordonneesBalle94[0]
        y94=coordonneesBalle94[1]

        coordonneesBalle95=monCanevas.bbox(balle95)
        x95=coordonneesBalle95[0]
        y95=coordonneesBalle95[1]

        coordonneesBalle96=monCanevas.bbox(balle96)
        x96=coordonneesBalle96[0]
        y96=coordonneesBalle96[1]

        coordonneesBalle97=monCanevas.bbox(balle97)
        x97=coordonneesBalle97[0]
        y97=coordonneesBalle97[1]

        coordonneesBalle98=monCanevas.bbox(balle98)
        x98=coordonneesBalle98[0]
        y98=coordonneesBalle98[1]

        coordonneesBalle99=monCanevas.bbox(balle99)
        x99=coordonneesBalle99[0]
        y99=coordonneesBalle99[1]

        coordonneesBalle100=monCanevas.bbox(balle100)
        x100=coordonneesBalle100[0]
        y100=coordonneesBalle100[1]

        coordonneesBalle101=monCanevas.bbox(balle101)
        x101=coordonneesBalle101[0]
        y101=coordonneesBalle101[1]

        coordonneesBalle102=monCanevas.bbox(balle102)
        x102=coordonneesBalle102[0]
        y102=coordonneesBalle102[1]

        coordonneesBalle103=monCanevas.bbox(balle103)
        x103=coordonneesBalle103[0]
        y103=coordonneesBalle103[1]

        coordonneesBalle104=monCanevas.bbox(balle104)
        x104=coordonneesBalle104[0]
        y104=coordonneesBalle104[1]

        coordonneesBalle105=monCanevas.bbox(balle105)
        x105=coordonneesBalle105[0]
        y105=coordonneesBalle105[1]

        coordonneesBalle106=monCanevas.bbox(balle106)
        x106=coordonneesBalle106[0]
        y106=coordonneesBalle106[1]

        coordonneesBalle107=monCanevas.bbox(balle107)
        x107=coordonneesBalle107[0]
        y107=coordonneesBalle107[1]

        coordonneesBalle108=monCanevas.bbox(balle108)
        x108=coordonneesBalle108[0]
        y108=coordonneesBalle108[1]

        coordonneesBalle109=monCanevas.bbox(balle109)
        x109=coordonneesBalle109[0]
        y109=coordonneesBalle109[1]

        coordonneesBalle110=monCanevas.bbox(balle110)
        x110=coordonneesBalle110[0]
        y110=coordonneesBalle110[1]

        coordonneesBalle111=monCanevas.bbox(balle111)
        x111=coordonneesBalle111[0]
        y111=coordonneesBalle111[1]

        coordonneesBalle112=monCanevas.bbox(balle112)
        x112=coordonneesBalle112[0]
        y112=coordonneesBalle112[1]

        coordonneesBalle113=monCanevas.bbox(balle113)
        x113=coordonneesBalle113[0]
        y113=coordonneesBalle113[1]

        coordonneesBalle114=monCanevas.bbox(balle114)
        x114=coordonneesBalle114[0]
        y114=coordonneesBalle114[1]

        coordonneesBalle115=monCanevas.bbox(balle115)
        x115=coordonneesBalle115[0]
        y115=coordonneesBalle115[1]

        coordonneesBalle116=monCanevas.bbox(balle116)
        x116=coordonneesBalle116[0]
        y116=coordonneesBalle116[1]

        coordonneesBalle117=monCanevas.bbox(balle117)
        x117=coordonneesBalle117[0]
        y117=coordonneesBalle117[1]

        coordonneesBalle118=monCanevas.bbox(balle118)
        x118=coordonneesBalle118[0]
        y118=coordonneesBalle118[1]

        coordonneesBalle119=monCanevas.bbox(balle119)
        x119=coordonneesBalle119[0]
        y119=coordonneesBalle119[1]

        coordonneesBalle120=monCanevas.bbox(balle120)
        x120=coordonneesBalle120[0]
        y120=coordonneesBalle120[1]

        coordonneesBalle121=monCanevas.bbox(balle121)
        x121=coordonneesBalle121[0]
        y121=coordonneesBalle121[1]

        coordonneesBalle122=monCanevas.bbox(balle122)
        x122=coordonneesBalle122[0]
        y122=coordonneesBalle122[1]

        coordonneesBalle123=monCanevas.bbox(balle123)
        x123=coordonneesBalle123[0]
        y123=coordonneesBalle123[1]

        coordonneesBalle124=monCanevas.bbox(balle124)
        x124=coordonneesBalle124[0]
        y124=coordonneesBalle124[1]

        coordonneesBalle125=monCanevas.bbox(balle125)
        x125=coordonneesBalle125[0]
        y125=coordonneesBalle125[1]

        coordonneesBalle126=monCanevas.bbox(balle126)
        x126=coordonneesBalle126[0]
        y126=coordonneesBalle126[1]

        coordonneesBalle127=monCanevas.bbox(balle127)
        x127=coordonneesBalle127[0]
        y127=coordonneesBalle127[1]

        coordonneesBalle128=monCanevas.bbox(balle128)
        x128=coordonneesBalle128[0]
        y128=coordonneesBalle128[1]

        coordonneesBalle129=monCanevas.bbox(balle129)
        x129=coordonneesBalle129[0]
        y129=coordonneesBalle129[1]

        coordonneesBalle130=monCanevas.bbox(balle130)
        x130=coordonneesBalle130[0]
        y130=coordonneesBalle130[1]

        coordonneesBalle131=monCanevas.bbox(balle131)
        x131=coordonneesBalle131[0]
        y131=coordonneesBalle131[1]

        coordonneesBalle132=monCanevas.bbox(balle132)
        x132=coordonneesBalle132[0]
        y132=coordonneesBalle132[1]

        coordonneesBalle133=monCanevas.bbox(balle133)
        x133=coordonneesBalle133[0]
        y133=coordonneesBalle133[1]

        coordonneesBalle134=monCanevas.bbox(balle134)
        x134=coordonneesBalle134[0]
        y134=coordonneesBalle134[1]

        coordonneesBalle135=monCanevas.bbox(balle135)
        x135=coordonneesBalle135[0]
        y135=coordonneesBalle135[1]

        coordonneesBalle136=monCanevas.bbox(balle136)
        x136=coordonneesBalle136[0]
        y136=coordonneesBalle136[1]

        coordonneesBalle137=monCanevas.bbox(balle137)
        x137=coordonneesBalle137[0]
        y137=coordonneesBalle137[1]

        coordonneesBalle138=monCanevas.bbox(balle138)
        x138=coordonneesBalle138[0]
        y138=coordonneesBalle138[1]

        coordonneesBalle139=monCanevas.bbox(balle139)
        x139=coordonneesBalle139[0]
        y139=coordonneesBalle139[1]

        coordonneesBalle140=monCanevas.bbox(balle140)
        x140=coordonneesBalle140[0]
        y140=coordonneesBalle140[1]

        coordonneesBalle141=monCanevas.bbox(balle141)
        x141=coordonneesBalle141[0]
        y141=coordonneesBalle141[1]

        coordonneesBalle142=monCanevas.bbox(balle142)
        x142=coordonneesBalle142[0]
        y142=coordonneesBalle142[1]

        coordonneesBalle143=monCanevas.bbox(balle143)
        x143=coordonneesBalle143[0]
        y143=coordonneesBalle143[1]

        coordonneesBalle144=monCanevas.bbox(balle144)
        x144=coordonneesBalle144[0]
        y144=coordonneesBalle144[1]

        coordonneesBalle145=monCanevas.bbox(balle145)
        x145=coordonneesBalle145[0]
        y145=coordonneesBalle145[1]

        coordonneesBalle146=monCanevas.bbox(balle146)
        x146=coordonneesBalle146[0]
        y146=coordonneesBalle146[1]

        coordonneesBalle147=monCanevas.bbox(balle147)
        x147=coordonneesBalle147[0]
        y147=coordonneesBalle147[1]

        coordonneesBalle148=monCanevas.bbox(balle148)
        x148=coordonneesBalle148[0]
        y148=coordonneesBalle148[1]

        coordonneesBalle149=monCanevas.bbox(balle149)
        x149=coordonneesBalle149[0]
        y149=coordonneesBalle149[1]

        coordonneesBalle150=monCanevas.bbox(balle150)
        x150=coordonneesBalle150[0]
        y150=coordonneesBalle150[1]

        coordonneesBalle151=monCanevas.bbox(balle151)
        x151=coordonneesBalle151[0]
        y151=coordonneesBalle151[1]

        coordonneesBalle152=monCanevas.bbox(balle152)
        x152=coordonneesBalle152[0]
        y152=coordonneesBalle152[1]

        coordonneesBalle153=monCanevas.bbox(balle153)
        x153=coordonneesBalle153[0]
        y153=coordonneesBalle153[1]

        coordonneesBalle154=monCanevas.bbox(balle154)
        x154=coordonneesBalle154[0]
        y154=coordonneesBalle154[1]

        coordonneesBalle155=monCanevas.bbox(balle155)
        x155=coordonneesBalle155[0]
        y155=coordonneesBalle155[1]

        coordonneesBalle156=monCanevas.bbox(balle156)
        x156=coordonneesBalle156[0]
        y156=coordonneesBalle156[1]

        coordonneesBalle157=monCanevas.bbox(balle157)
        x157=coordonneesBalle157[0]
        y157=coordonneesBalle157[1]

        coordonneesBalle158=monCanevas.bbox(balle158)
        x158=coordonneesBalle158[0]
        y158=coordonneesBalle158[1]

        coordonneesBalle159=monCanevas.bbox(balle159)
        x159=coordonneesBalle159[0]
        y159=coordonneesBalle159[1]

        coordonneesBalle160=monCanevas.bbox(balle160)
        x160=coordonneesBalle160[0]
        y160=coordonneesBalle160[1]

        coordonneesBalle161=monCanevas.bbox(balle161)
        x161=coordonneesBalle161[0]
        y161=coordonneesBalle161[1]

        coordonneesBalle162=monCanevas.bbox(balle162)
        x162=coordonneesBalle162[0]
        y162=coordonneesBalle162[1]

        coordonneesBalle163=monCanevas.bbox(balle163)
        x163=coordonneesBalle163[0]
        y163=coordonneesBalle163[1]

        coordonneesBalle164=monCanevas.bbox(balle164)
        x164=coordonneesBalle164[0]
        y164=coordonneesBalle164[1]

        coordonneesBalle165=monCanevas.bbox(balle165)
        x165=coordonneesBalle165[0]
        y165=coordonneesBalle165[1]

        coordonneesBalle166=monCanevas.bbox(balle166)
        x166=coordonneesBalle166[0]
        y166=coordonneesBalle166[1]

        coordonneesBalle167=monCanevas.bbox(balle167)
        x167=coordonneesBalle167[0]
        y167=coordonneesBalle167[1]

        coordonneesBalle168=monCanevas.bbox(balle168)
        x168=coordonneesBalle168[0]
        y168=coordonneesBalle168[1]

        coordonneesBalle169=monCanevas.bbox(balle169)
        x169=coordonneesBalle169[0]
        y169=coordonneesBalle169[1]

        coordonneesBalle170=monCanevas.bbox(balle170)
        x170=coordonneesBalle170[0]
        y170=coordonneesBalle170[1]

        coordonneesBalle171=monCanevas.bbox(balle171)
        x171=coordonneesBalle171[0]
        y171=coordonneesBalle171[1]

        coordonneesBalle172=monCanevas.bbox(balle172)
        x172=coordonneesBalle172[0]
        y172=coordonneesBalle172[1]

        coordonneesBalle173=monCanevas.bbox(balle173)
        x173=coordonneesBalle173[0]
        y173=coordonneesBalle173[1]

        coordonneesBalle174=monCanevas.bbox(balle174)
        x174=coordonneesBalle174[0]
        y174=coordonneesBalle174[1]

        coordonneesBalle175=monCanevas.bbox(balle175)
        x175=coordonneesBalle175[0]
        y175=coordonneesBalle175[1]

        coordonneesBalle176=monCanevas.bbox(balle176)
        x176=coordonneesBalle176[0]
        y176=coordonneesBalle176[1]

        coordonneesBalle177=monCanevas.bbox(balle177)
        x177=coordonneesBalle177[0]
        y177=coordonneesBalle177[1]

        coordonneesBalle178=monCanevas.bbox(balle178)
        x178=coordonneesBalle178[0]
        y178=coordonneesBalle178[1]

        coordonneesBalle179=monCanevas.bbox(balle179)
        x179=coordonneesBalle179[0]
        y179=coordonneesBalle179[1]

        coordonneesBalle180=monCanevas.bbox(balle180)
        x180=coordonneesBalle180[0]
        y180=coordonneesBalle180[1]

        coordonneesBalle181=monCanevas.bbox(balle181)
        x181=coordonneesBalle181[0]
        y181=coordonneesBalle181[1]

        coordonneesBalle182=monCanevas.bbox(balle182)
        x182=coordonneesBalle182[0]
        y182=coordonneesBalle182[1]

        coordonneesBalle183=monCanevas.bbox(balle183)
        x183=coordonneesBalle183[0]
        y183=coordonneesBalle183[1]

        coordonneesBalle184=monCanevas.bbox(balle184)
        x184=coordonneesBalle184[0]
        y184=coordonneesBalle184[1]

        coordonneesBalle185=monCanevas.bbox(balle185)
        x185=coordonneesBalle185[0]
        y185=coordonneesBalle185[1]

        coordonneesBalle186=monCanevas.bbox(balle186)
        x186=coordonneesBalle186[0]
        y186=coordonneesBalle186[1]

        coordonneesBalle187=monCanevas.bbox(balle187)
        x187=coordonneesBalle187[0]
        y187=coordonneesBalle187[1]

        coordonneesBalle188=monCanevas.bbox(balle188)
        x188=coordonneesBalle188[0]
        y188=coordonneesBalle188[1]

        coordonneesBalle189=monCanevas.bbox(balle189)
        x189=coordonneesBalle189[0]
        y189=coordonneesBalle189[1]

        coordonneesBalle190=monCanevas.bbox(balle190)
        x190=coordonneesBalle190[0]
        y190=coordonneesBalle190[1]

        coordonneesBalle191=monCanevas.bbox(balle191)
        x191=coordonneesBalle191[0]
        y191=coordonneesBalle191[1]

        coordonneesBalle192=monCanevas.bbox(balle192)
        x192=coordonneesBalle192[0]
        y192=coordonneesBalle192[1]

        coordonneesBalle193=monCanevas.bbox(balle193)
        x193=coordonneesBalle193[0]
        y193=coordonneesBalle193[1]

        coordonneesBalle194=monCanevas.bbox(balle194)
        x194=coordonneesBalle194[0]
        y194=coordonneesBalle194[1]

        coordonneesBalle195=monCanevas.bbox(balle195)
        x195=coordonneesBalle195[0]
        y195=coordonneesBalle195[1]

        coordonneesBalle196=monCanevas.bbox(balle196)
        x196=coordonneesBalle196[0]
        y196=coordonneesBalle196[1]

        coordonneesBalle197=monCanevas.bbox(balle197)
        x197=coordonneesBalle197[0]
        y197=coordonneesBalle197[1]

        coordonneesBalle198=monCanevas.bbox(balle198)
        x198=coordonneesBalle198[0]
        y198=coordonneesBalle198[1]

        coordonneesBalle199=monCanevas.bbox(balle199)
        x199=coordonneesBalle199[0]
        y199=coordonneesBalle199[1]

        coordonneesBalle200=monCanevas.bbox(balle200)
        x200=coordonneesBalle200[0]
        y200=coordonneesBalle200[1]

        coordonneesBalle201=monCanevas.bbox(balle201)
        x201=coordonneesBalle201[0]
        y201=coordonneesBalle201[1]

        coordonneesBalle202=monCanevas.bbox(balle202)
        x202=coordonneesBalle202[0]
        y202=coordonneesBalle202[1]

        coordonneesBalle203=monCanevas.bbox(balle203)
        x203=coordonneesBalle203[0]
        y203=coordonneesBalle203[1]

        coordonneesBalle204=monCanevas.bbox(balle204)
        x204=coordonneesBalle204[0]
        y204=coordonneesBalle204[1]

        coordonneesBalle205=monCanevas.bbox(balle205)
        x205=coordonneesBalle205[0]
        y205=coordonneesBalle205[1]

        coordonneesBalle206=monCanevas.bbox(balle206)
        x206=coordonneesBalle206[0]
        y206=coordonneesBalle206[1]

        coordonneesBalle207=monCanevas.bbox(balle207)
        x207=coordonneesBalle207[0]
        y207=coordonneesBalle207[1]

        coordonneesBalle208=monCanevas.bbox(balle208)
        x208=coordonneesBalle208[0]
        y208=coordonneesBalle208[1]

        coordonneesBalle209=monCanevas.bbox(balle209)
        x209=coordonneesBalle209[0]
        y209=coordonneesBalle209[1]

        coordonneesBalle210=monCanevas.bbox(balle210)
        x210=coordonneesBalle210[0]
        y210=coordonneesBalle210[1]

        coordonneesBalle211=monCanevas.bbox(balle211)
        x211=coordonneesBalle211[0]
        y211=coordonneesBalle211[1]

        coordonneesBalle212=monCanevas.bbox(balle212)
        x212=coordonneesBalle212[0]
        y212=coordonneesBalle212[1]

        coordonneesBalle213=monCanevas.bbox(balle213)
        x213=coordonneesBalle213[0]
        y213=coordonneesBalle213[1]

        coordonneesBalle214=monCanevas.bbox(balle214)
        x214=coordonneesBalle214[0]
        y214=coordonneesBalle214[1]

        coordonneesBalle215=monCanevas.bbox(balle215)
        x215=coordonneesBalle215[0]
        y215=coordonneesBalle215[1]

        coordonneesBalle216=monCanevas.bbox(balle216)
        x216=coordonneesBalle216[0]
        y216=coordonneesBalle216[1]

        coordonneesBalle217=monCanevas.bbox(balle217)
        x217=coordonneesBalle217[0]
        y217=coordonneesBalle217[1]

        coordonneesBalle218=monCanevas.bbox(balle218)
        x218=coordonneesBalle218[0]
        y218=coordonneesBalle218[1]

        coordonneesBalle219=monCanevas.bbox(balle219)
        x219=coordonneesBalle219[0]
        y219=coordonneesBalle219[1]

        coordonneesBalle220=monCanevas.bbox(balle220)
        x220=coordonneesBalle220[0]
        y220=coordonneesBalle220[1]

        coordonneesBalle221=monCanevas.bbox(balle221)
        x221=coordonneesBalle221[0]
        y221=coordonneesBalle221[1]

        coordonneesBalle222=monCanevas.bbox(balle222)
        x222=coordonneesBalle222[0]
        y222=coordonneesBalle222[1]

        coordonneesBalle223=monCanevas.bbox(balle223)
        x223=coordonneesBalle223[0]
        y223=coordonneesBalle223[1]

        coordonneesBalle224=monCanevas.bbox(balle224)
        x224=coordonneesBalle224[0]
        y224=coordonneesBalle224[1]

        coordonneesBalle225=monCanevas.bbox(balle225)
        x225=coordonneesBalle225[0]
        y225=coordonneesBalle225[1]

        coordonneesBalle226=monCanevas.bbox(balle226)
        x226=coordonneesBalle226[0]
        y226=coordonneesBalle226[1]

        coordonneesBalle227=monCanevas.bbox(balle227)
        x227=coordonneesBalle227[0]
        y227=coordonneesBalle227[1]

        coordonneesBalle228=monCanevas.bbox(balle228)
        x228=coordonneesBalle228[0]
        y228=coordonneesBalle228[1]

        coordonneesBalle229=monCanevas.bbox(balle229)
        x229=coordonneesBalle229[0]
        y229=coordonneesBalle229[1]

        coordonneesBalle230=monCanevas.bbox(balle230)
        x230=coordonneesBalle230[0]
        y230=coordonneesBalle230[1]

        coordonneesBalle231=monCanevas.bbox(balle231)
        x231=coordonneesBalle231[0]
        y231=coordonneesBalle231[1]

        coordonneesBalle232=monCanevas.bbox(balle232)
        x232=coordonneesBalle232[0]
        y232=coordonneesBalle232[1]

        coordonneesBalle233=monCanevas.bbox(balle233)
        x233=coordonneesBalle233[0]
        y233=coordonneesBalle233[1]

        coordonneesBalle234=monCanevas.bbox(balle234)
        x234=coordonneesBalle234[0]
        y234=coordonneesBalle234[1]

        coordonneesBalle235=monCanevas.bbox(balle235)
        x235=coordonneesBalle235[0]
        y235=coordonneesBalle235[1]

        coordonneesBalle236=monCanevas.bbox(balle236)
        x236=coordonneesBalle236[0]
        y236=coordonneesBalle236[1]

        coordonneesBalle237=monCanevas.bbox(balle237)
        x237=coordonneesBalle237[0]
        y237=coordonneesBalle237[1]

        coordonneesBalle238=monCanevas.bbox(balle238)
        x238=coordonneesBalle238[0]
        y238=coordonneesBalle238[1]

        coordonneesBalle239=monCanevas.bbox(balle239)
        x239=coordonneesBalle239[0]
        y239=coordonneesBalle239[1]

        coordonneesBalle240=monCanevas.bbox(balle240)
        x240=coordonneesBalle240[0]
        y240=coordonneesBalle240[1]

        coordonneesBalle241=monCanevas.bbox(balle241)
        x241=coordonneesBalle241[0]
        y241=coordonneesBalle241[1]

        coordonneesBalle242=monCanevas.bbox(balle242)
        x242=coordonneesBalle242[0]
        y242=coordonneesBalle242[1]

        coordonneesBalle243=monCanevas.bbox(balle243)
        x243=coordonneesBalle243[0]
        y243=coordonneesBalle243[1]

        coordonneesBalle244=monCanevas.bbox(balle244)
        x244=coordonneesBalle244[0]
        y244=coordonneesBalle244[1]

        coordonneesBalle245=monCanevas.bbox(balle245)
        x245=coordonneesBalle245[0]
        y245=coordonneesBalle245[1]

        coordonneesBalle246=monCanevas.bbox(balle246)
        x246=coordonneesBalle246[0]
        y246=coordonneesBalle246[1]

        coordonneesBalle247=monCanevas.bbox(balle247)
        x247=coordonneesBalle247[0]
        y247=coordonneesBalle247[1]

        coordonneesBalle248=monCanevas.bbox(balle248)
        x248=coordonneesBalle248[0]
        y248=coordonneesBalle248[1]

        coordonneesBalle249=monCanevas.bbox(balle249)
        x249=coordonneesBalle249[0]
        y249=coordonneesBalle249[1]

        coordonneesBalle250=monCanevas.bbox(balle250)
        x250=coordonneesBalle250[0]
        y250=coordonneesBalle250[1]

        coordonneesBalle251=monCanevas.bbox(balle251)
        x251=coordonneesBalle251[0]
        y251=coordonneesBalle251[1]

        coordonneesBalle252=monCanevas.bbox(balle252)
        x252=coordonneesBalle252[0]
        y252=coordonneesBalle252[1]

        coordonneesBalle253=monCanevas.bbox(balle253)
        x253=coordonneesBalle253[0]
        y253=coordonneesBalle253[1]

        coordonneesBalle254=monCanevas.bbox(balle254)
        x254=coordonneesBalle254[0]
        y254=coordonneesBalle254[1]

        coordonneesBalle255=monCanevas.bbox(balle255)
        x255=coordonneesBalle255[0]
        y255=coordonneesBalle255[1]

        coordonneesBalle256=monCanevas.bbox(balle256)
        x256=coordonneesBalle256[0]
        y256=coordonneesBalle256[1]

        coordonneesBalle257=monCanevas.bbox(balle257)
        x257=coordonneesBalle257[0]
        y257=coordonneesBalle257[1]

        coordonneesBalle258=monCanevas.bbox(balle258)
        x258=coordonneesBalle258[0]
        y258=coordonneesBalle258[1]

        coordonneesBalle259=monCanevas.bbox(balle259)
        x259=coordonneesBalle259[0]
        y259=coordonneesBalle259[1]

        coordonneesBalle260=monCanevas.bbox(balle260)
        x260=coordonneesBalle260[0]
        y260=coordonneesBalle260[1]

        coordonneesBalle261=monCanevas.bbox(balle261)
        x261=coordonneesBalle261[0]
        y261=coordonneesBalle261[1]

        coordonneesBalle262=monCanevas.bbox(balle262)
        x262=coordonneesBalle262[0]
        y262=coordonneesBalle262[1]

        coordonneesBalle263=monCanevas.bbox(balle263)
        x263=coordonneesBalle263[0]
        y263=coordonneesBalle263[1]

        coordonneesBalle264=monCanevas.bbox(balle264)
        x264=coordonneesBalle264[0]
        y264=coordonneesBalle264[1]

        coordonneesBalle265=monCanevas.bbox(balle265)
        x265=coordonneesBalle265[0]
        y265=coordonneesBalle265[1]

        coordonneesBalle266=monCanevas.bbox(balle266)
        x266=coordonneesBalle266[0]
        y266=coordonneesBalle266[1]

        coordonneesBalle267=monCanevas.bbox(balle267)
        x267=coordonneesBalle267[0]
        y267=coordonneesBalle267[1]

        coordonneesBalle268=monCanevas.bbox(balle268)
        x268=coordonneesBalle268[0]
        y268=coordonneesBalle268[1]

        coordonneesBalle269=monCanevas.bbox(balle269)
        x269=coordonneesBalle269[0]
        y269=coordonneesBalle269[1]

        coordonneesBalle270=monCanevas.bbox(balle270)
        x270=coordonneesBalle270[0]
        y270=coordonneesBalle270[1]

        coordonneesBalle271=monCanevas.bbox(balle271)
        x271=coordonneesBalle271[0]
        y271=coordonneesBalle271[1]

        coordonneesBalle272=monCanevas.bbox(balle272)
        x272=coordonneesBalle272[0]
        y272=coordonneesBalle272[1]

        coordonneesBalle273=monCanevas.bbox(balle273)
        x273=coordonneesBalle273[0]
        y273=coordonneesBalle273[1]

        coordonneesBalle274=monCanevas.bbox(balle274)
        x274=coordonneesBalle274[0]
        y274=coordonneesBalle274[1]

        coordonneesBalle275=monCanevas.bbox(balle275)
        x275=coordonneesBalle275[0]
        y275=coordonneesBalle275[1]

        coordonneesBalle276=monCanevas.bbox(balle276)
        x276=coordonneesBalle276[0]
        y276=coordonneesBalle276[1]

        coordonneesBalle277=monCanevas.bbox(balle277)
        x277=coordonneesBalle277[0]
        y277=coordonneesBalle277[1]

        coordonneesBalle278=monCanevas.bbox(balle278)
        x278=coordonneesBalle278[0]
        y278=coordonneesBalle278[1]

        coordonneesBalle279=monCanevas.bbox(balle279)
        x279=coordonneesBalle279[0]
        y279=coordonneesBalle279[1]

        coordonneesBalle280=monCanevas.bbox(balle280)
        x280=coordonneesBalle280[0]
        y280=coordonneesBalle280[1]

        coordonneesBalle281=monCanevas.bbox(balle281)
        x281=coordonneesBalle281[0]
        y281=coordonneesBalle281[1]

        coordonneesBalle282=monCanevas.bbox(balle282)
        x282=coordonneesBalle282[0]
        y282=coordonneesBalle282[1]

        coordonneesBalle283=monCanevas.bbox(balle283)
        x283=coordonneesBalle283[0]
        y283=coordonneesBalle283[1]

        coordonneesBalle284=monCanevas.bbox(balle284)
        x284=coordonneesBalle284[0]
        y284=coordonneesBalle284[1]

        coordonneesBalle285=monCanevas.bbox(balle285)
        x285=coordonneesBalle285[0]
        y285=coordonneesBalle285[1]

        coordonneesBalle286=monCanevas.bbox(balle286)
        x286=coordonneesBalle286[0]
        y286=coordonneesBalle286[1]

        coordonneesBalle287=monCanevas.bbox(balle287)
        x287=coordonneesBalle287[0]
        y287=coordonneesBalle287[1]

        coordonneesBalle288=monCanevas.bbox(balle288)
        x288=coordonneesBalle288[0]
        y288=coordonneesBalle288[1]

        coordonneesBalle289=monCanevas.bbox(balle289)
        x289=coordonneesBalle289[0]
        y289=coordonneesBalle289[1]

        coordonneesBalle290=monCanevas.bbox(balle290)
        x290=coordonneesBalle290[0]
        y290=coordonneesBalle290[1]

        coordonneesBalle291=monCanevas.bbox(balle291)
        x291=coordonneesBalle291[0]
        y291=coordonneesBalle291[1]

        coordonneesBalle292=monCanevas.bbox(balle292)
        x292=coordonneesBalle292[0]
        y292=coordonneesBalle292[1]

        coordonneesBalle293=monCanevas.bbox(balle293)
        x293=coordonneesBalle293[0]
        y293=coordonneesBalle293[1]

        coordonneesBalle294=monCanevas.bbox(balle294)
        x294=coordonneesBalle294[0]
        y294=coordonneesBalle294[1]

        coordonneesBalle295=monCanevas.bbox(balle295)
        x295=coordonneesBalle295[0]
        y295=coordonneesBalle295[1]

        coordonneesBalle296=monCanevas.bbox(balle296)
        x296=coordonneesBalle296[0]
        y296=coordonneesBalle296[1]

        coordonneesBalle297=monCanevas.bbox(balle297)
        x297=coordonneesBalle297[0]
        y297=coordonneesBalle297[1]

        coordonneesBalle298=monCanevas.bbox(balle298)
        x298=coordonneesBalle298[0]
        y298=coordonneesBalle298[1]

        coordonneesBalle299=monCanevas.bbox(balle299)
        x299=coordonneesBalle299[0]
        y299=coordonneesBalle299[1]

        coordonneesBalle300=monCanevas.bbox(balle300)
        x300=coordonneesBalle300[0]
        y300=coordonneesBalle300[1]

        coordonneesBalle301=monCanevas.bbox(balle301)
        x301=coordonneesBalle301[0]
        y301=coordonneesBalle301[1]

        coordonneesBalle302=monCanevas.bbox(balle302)
        x302=coordonneesBalle302[0]
        y302=coordonneesBalle302[1]

        coordonneesBalle303=monCanevas.bbox(balle303)
        x303=coordonneesBalle303[0]
        y303=coordonneesBalle303[1]

        coordonneesBalle304=monCanevas.bbox(balle304)
        x304=coordonneesBalle304[0]
        y304=coordonneesBalle304[1]

        coordonneesBalle305=monCanevas.bbox(balle305)
        x305=coordonneesBalle305[0]
        y305=coordonneesBalle305[1]

        coordonneesBalle306=monCanevas.bbox(balle306)
        x306=coordonneesBalle306[0]
        y306=coordonneesBalle306[1]

        coordonneesBalle307=monCanevas.bbox(balle307)
        x307=coordonneesBalle307[0]
        y307=coordonneesBalle307[1]

        coordonneesBalle308=monCanevas.bbox(balle308)
        x308=coordonneesBalle308[0]
        y308=coordonneesBalle308[1]

        coordonneesBalle309=monCanevas.bbox(balle309)
        x309=coordonneesBalle309[0]
        y309=coordonneesBalle309[1]

        coordonneesBalle310=monCanevas.bbox(balle310)
        x310=coordonneesBalle310[0]
        y310=coordonneesBalle310[1]

        coordonneesBalle311=monCanevas.bbox(balle311)
        x311=coordonneesBalle311[0]
        y311=coordonneesBalle311[1]

        coordonneesBalle312=monCanevas.bbox(balle312)
        x312=coordonneesBalle312[0]
        y312=coordonneesBalle312[1]

        coordonneesBalle313=monCanevas.bbox(balle313)
        x313=coordonneesBalle313[0]
        y313=coordonneesBalle313[1]

        coordonneesBalle314=monCanevas.bbox(balle314)
        x314=coordonneesBalle314[0]
        y314=coordonneesBalle314[1]

        coordonneesBalle315=monCanevas.bbox(balle315)
        x315=coordonneesBalle315[0]
        y315=coordonneesBalle315[1]

        coordonneesBalle316=monCanevas.bbox(balle316)
        x316=coordonneesBalle316[0]
        y316=coordonneesBalle316[1]

        coordonneesBalle317=monCanevas.bbox(balle317)
        x317=coordonneesBalle317[0]
        y317=coordonneesBalle317[1]

        coordonneesBalle318=monCanevas.bbox(balle318)
        x318=coordonneesBalle318[0]
        y318=coordonneesBalle318[1]

        coordonneesBalle319=monCanevas.bbox(balle319)
        x319=coordonneesBalle319[0]
        y319=coordonneesBalle319[1]

        coordonneesBalle320=monCanevas.bbox(balle320)
        x320=coordonneesBalle320[0]
        y320=coordonneesBalle320[1]

        coordonneesBalle321=monCanevas.bbox(balle321)
        x321=coordonneesBalle321[0]
        y321=coordonneesBalle321[1]

        coordonneesBalle322=monCanevas.bbox(balle322)
        x322=coordonneesBalle322[0]
        y322=coordonneesBalle322[1]

        coordonneesBalle323=monCanevas.bbox(balle323)
        x323=coordonneesBalle323[0]
        y323=coordonneesBalle323[1]

        coordonneesBalle324=monCanevas.bbox(balle324)
        x324=coordonneesBalle324[0]
        y324=coordonneesBalle324[1]

        coordonneesBalle325=monCanevas.bbox(balle325)
        x325=coordonneesBalle325[0]
        y325=coordonneesBalle325[1]

        coordonneesBalle326=monCanevas.bbox(balle326)
        x326=coordonneesBalle326[0]
        y326=coordonneesBalle326[1]

        coordonneesBalle327=monCanevas.bbox(balle327)
        x327=coordonneesBalle327[0]
        y327=coordonneesBalle327[1]

        coordonneesBalle328=monCanevas.bbox(balle328)
        x328=coordonneesBalle328[0]
        y328=coordonneesBalle328[1]

        coordonneesBalle329=monCanevas.bbox(balle329)
        x329=coordonneesBalle329[0]
        y329=coordonneesBalle329[1]

        coordonneesBalle330=monCanevas.bbox(balle330)
        x330=coordonneesBalle330[0]
        y330=coordonneesBalle330[1]

        coordonneesBalle331=monCanevas.bbox(balle331)
        x331=coordonneesBalle331[0]
        y331=coordonneesBalle331[1]

        coordonneesBalle332=monCanevas.bbox(balle332)
        x332=coordonneesBalle332[0]
        y332=coordonneesBalle332[1]

        coordonneesBalle333=monCanevas.bbox(balle333)
        x333=coordonneesBalle333[0]
        y333=coordonneesBalle333[1]

        coordonneesBalle334=monCanevas.bbox(balle334)
        x334=coordonneesBalle334[0]
        y334=coordonneesBalle334[1]

        coordonneesBalle335=monCanevas.bbox(balle335)
        x335=coordonneesBalle335[0]
        y335=coordonneesBalle335[1]

        coordonneesBalle336=monCanevas.bbox(balle336)
        x336=coordonneesBalle336[0]
        y336=coordonneesBalle336[1]

        coordonneesBalle337=monCanevas.bbox(balle337)
        x337=coordonneesBalle337[0]
        y337=coordonneesBalle337[1]

        coordonneesBalle338=monCanevas.bbox(balle338)
        x338=coordonneesBalle338[0]
        y338=coordonneesBalle338[1]

        coordonneesBalle339=monCanevas.bbox(balle339)
        x339=coordonneesBalle339[0]
        y339=coordonneesBalle339[1]

        coordonneesBalle340=monCanevas.bbox(balle340)
        x340=coordonneesBalle340[0]
        y340=coordonneesBalle340[1]

        coordonneesBalle341=monCanevas.bbox(balle341)
        x341=coordonneesBalle341[0]
        y341=coordonneesBalle341[1]

        coordonneesBalle342=monCanevas.bbox(balle342)
        x342=coordonneesBalle342[0]
        y342=coordonneesBalle342[1]

        coordonneesBalle343=monCanevas.bbox(balle343)
        x343=coordonneesBalle343[0]
        y343=coordonneesBalle343[1]

        coordonneesBalle344=monCanevas.bbox(balle344)
        x344=coordonneesBalle344[0]
        y344=coordonneesBalle344[1]

        coordonneesBalle345=monCanevas.bbox(balle345)
        x345=coordonneesBalle345[0]
        y345=coordonneesBalle345[1]

        coordonneesBalle346=monCanevas.bbox(balle346)
        x346=coordonneesBalle346[0]
        y346=coordonneesBalle346[1]

        coordonneesBalle347=monCanevas.bbox(balle347)
        x347=coordonneesBalle347[0]
        y347=coordonneesBalle347[1]

        coordonneesBalle348=monCanevas.bbox(balle348)
        x348=coordonneesBalle348[0]
        y348=coordonneesBalle348[1]

        coordonneesBalle349=monCanevas.bbox(balle349)
        x349=coordonneesBalle349[0]
        y349=coordonneesBalle349[1]

        coordonneesBalle350=monCanevas.bbox(balle350)
        x350=coordonneesBalle350[0]
        y350=coordonneesBalle350[1]

        coordonneesBalle351=monCanevas.bbox(balle351)
        x351=coordonneesBalle351[0]
        y351=coordonneesBalle351[1]

        coordonneesBalle352=monCanevas.bbox(balle352)
        x352=coordonneesBalle352[0]
        y352=coordonneesBalle352[1]

        coordonneesBalle353=monCanevas.bbox(balle353)
        x353=coordonneesBalle353[0]
        y353=coordonneesBalle353[1]

        coordonneesBalle354=monCanevas.bbox(balle354)
        x354=coordonneesBalle354[0]
        y354=coordonneesBalle354[1]

        coordonneesBalle355=monCanevas.bbox(balle355)
        x355=coordonneesBalle355[0]
        y355=coordonneesBalle355[1]

        coordonneesBalle356=monCanevas.bbox(balle356)
        x356=coordonneesBalle356[0]
        y356=coordonneesBalle356[1]

        coordonneesBalle357=monCanevas.bbox(balle357)
        x357=coordonneesBalle357[0]
        y357=coordonneesBalle357[1]

        coordonneesBalle358=monCanevas.bbox(balle358)
        x358=coordonneesBalle358[0]
        y358=coordonneesBalle358[1]

        coordonneesBalle359=monCanevas.bbox(balle359)
        x359=coordonneesBalle359[0]
        y359=coordonneesBalle359[1]

        coordonneesBalle360=monCanevas.bbox(balle360)
        x360=coordonneesBalle360[0]
        y360=coordonneesBalle360[1]

        coordonneesBalle361=monCanevas.bbox(balle361)
        x361=coordonneesBalle361[0]
        y361=coordonneesBalle361[1]

        coordonneesBalle362=monCanevas.bbox(balle362)
        x362=coordonneesBalle362[0]
        y362=coordonneesBalle362[1]

        coordonneesBalle363=monCanevas.bbox(balle363)
        x363=coordonneesBalle363[0]
        y363=coordonneesBalle363[1]

        coordonneesBalle364=monCanevas.bbox(balle364)
        x364=coordonneesBalle364[0]
        y364=coordonneesBalle364[1]

        coordonneesBalle365=monCanevas.bbox(balle365)
        x365=coordonneesBalle365[0]
        y365=coordonneesBalle365[1]

        coordonneesBalle366=monCanevas.bbox(balle366)
        x366=coordonneesBalle366[0]
        y366=coordonneesBalle366[1]

        coordonneesBalle367=monCanevas.bbox(balle367)
        x367=coordonneesBalle367[0]
        y367=coordonneesBalle367[1]

        coordonneesBalle368=monCanevas.bbox(balle368)
        x368=coordonneesBalle368[0]
        y368=coordonneesBalle368[1]

        coordonneesBalle369=monCanevas.bbox(balle369)
        x369=coordonneesBalle369[0]
        y369=coordonneesBalle369[1]

        coordonneesBalle370=monCanevas.bbox(balle370)
        x370=coordonneesBalle370[0]
        y370=coordonneesBalle370[1]

        coordonneesBalle371=monCanevas.bbox(balle371)
        x371=coordonneesBalle371[0]
        y371=coordonneesBalle371[1]

        coordonneesBalle372=monCanevas.bbox(balle372)
        x372=coordonneesBalle372[0]
        y372=coordonneesBalle372[1]

        coordonneesBalle373=monCanevas.bbox(balle373)
        x373=coordonneesBalle373[0]
        y373=coordonneesBalle373[1]

        coordonneesBalle374=monCanevas.bbox(balle374)
        x374=coordonneesBalle374[0]
        y374=coordonneesBalle374[1]

        coordonneesBalle375=monCanevas.bbox(balle375)
        x375=coordonneesBalle375[0]
        y375=coordonneesBalle375[1]

        coordonneesBalle376=monCanevas.bbox(balle376)
        x376=coordonneesBalle376[0]
        y376=coordonneesBalle376[1]

        coordonneesBalle377=monCanevas.bbox(balle377)
        x377=coordonneesBalle377[0]
        y377=coordonneesBalle377[1]

        coordonneesBalle378=monCanevas.bbox(balle378)
        x378=coordonneesBalle378[0]
        y378=coordonneesBalle378[1]

        coordonneesBalle379=monCanevas.bbox(balle379)
        x379=coordonneesBalle379[0]
        y379=coordonneesBalle379[1]

        coordonneesBalle380=monCanevas.bbox(balle380)
        x380=coordonneesBalle380[0]
        y380=coordonneesBalle380[1]

        coordonneesBalle381=monCanevas.bbox(balle381)
        x381=coordonneesBalle381[0]
        y381=coordonneesBalle381[1]

        coordonneesBalle382=monCanevas.bbox(balle382)
        x382=coordonneesBalle382[0]
        y382=coordonneesBalle382[1]

        coordonneesBalle383=monCanevas.bbox(balle383)
        x383=coordonneesBalle383[0]
        y383=coordonneesBalle383[1]

        coordonneesBalle384=monCanevas.bbox(balle384)
        x384=coordonneesBalle384[0]
        y384=coordonneesBalle384[1]

        coordonneesBalle385=monCanevas.bbox(balle385)
        x385=coordonneesBalle385[0]
        y385=coordonneesBalle385[1]

        coordonneesBalle386=monCanevas.bbox(balle386)
        x386=coordonneesBalle386[0]
        y386=coordonneesBalle386[1]

        coordonneesBalle387=monCanevas.bbox(balle387)
        x387=coordonneesBalle387[0]
        y387=coordonneesBalle387[1]

        coordonneesBalle388=monCanevas.bbox(balle388)
        x388=coordonneesBalle388[0]
        y388=coordonneesBalle388[1]

        coordonneesBalle389=monCanevas.bbox(balle389)
        x389=coordonneesBalle389[0]
        y389=coordonneesBalle389[1]

        coordonneesBalle390=monCanevas.bbox(balle390)
        x390=coordonneesBalle390[0]
        y390=coordonneesBalle390[1]

        coordonneesBalle391=monCanevas.bbox(balle391)
        x391=coordonneesBalle391[0]
        y391=coordonneesBalle391[1]

        coordonneesBalle392=monCanevas.bbox(balle392)
        x392=coordonneesBalle392[0]
        y392=coordonneesBalle392[1]

        coordonneesBalle393=monCanevas.bbox(balle393)
        x393=coordonneesBalle393[0]
        y393=coordonneesBalle393[1]

        coordonneesBalle394=monCanevas.bbox(balle394)
        x394=coordonneesBalle394[0]
        y394=coordonneesBalle394[1]

        coordonneesBalle395=monCanevas.bbox(balle395)
        x395=coordonneesBalle395[0]
        y395=coordonneesBalle395[1]

        coordonneesBalle396=monCanevas.bbox(balle396)
        x396=coordonneesBalle396[0]
        y396=coordonneesBalle396[1]

        coordonneesBalle397=monCanevas.bbox(balle397)
        x397=coordonneesBalle397[0]
        y397=coordonneesBalle397[1]

        coordonneesBalle398=monCanevas.bbox(balle398)
        x398=coordonneesBalle398[0]
        y398=coordonneesBalle398[1]

        coordonneesBalle399=monCanevas.bbox(balle399)
        x399=coordonneesBalle399[0]
        y399=coordonneesBalle399[1]

        coordonneesBalle400=monCanevas.bbox(balle400)
        x400=coordonneesBalle400[0]
        y400=coordonneesBalle400[1]

        coordonneesBalle401=monCanevas.bbox(balle401)
        x401=coordonneesBalle401[0]
        y401=coordonneesBalle401[1]

        coordonneesBalle402=monCanevas.bbox(balle402)
        x402=coordonneesBalle402[0]
        y402=coordonneesBalle402[1]

        coordonneesBalle403=monCanevas.bbox(balle403)
        x403=coordonneesBalle403[0]
        y403=coordonneesBalle403[1]

        coordonneesBalle404=monCanevas.bbox(balle404)
        x404=coordonneesBalle404[0]
        y404=coordonneesBalle404[1]

        coordonneesBalle405=monCanevas.bbox(balle405)
        x405=coordonneesBalle405[0]
        y405=coordonneesBalle405[1]

        coordonneesBalle406=monCanevas.bbox(balle406)
        x406=coordonneesBalle406[0]
        y406=coordonneesBalle406[1]

        coordonneesBalle407=monCanevas.bbox(balle407)
        x407=coordonneesBalle407[0]
        y407=coordonneesBalle407[1]

        coordonneesBalle408=monCanevas.bbox(balle408)
        x408=coordonneesBalle408[0]
        y408=coordonneesBalle408[1]

        coordonneesBalle409=monCanevas.bbox(balle409)
        x409=coordonneesBalle409[0]
        y409=coordonneesBalle409[1]

        coordonneesBalle410=monCanevas.bbox(balle410)
        x410=coordonneesBalle410[0]
        y410=coordonneesBalle410[1]

        coordonneesBalle411=monCanevas.bbox(balle411)
        x411=coordonneesBalle411[0]
        y411=coordonneesBalle411[1]

        coordonneesBalle412=monCanevas.bbox(balle412)
        x412=coordonneesBalle412[0]
        y412=coordonneesBalle412[1]

        coordonneesBalle413=monCanevas.bbox(balle413)
        x413=coordonneesBalle413[0]
        y413=coordonneesBalle413[1]

        coordonneesBalle414=monCanevas.bbox(balle414)
        x414=coordonneesBalle414[0]
        y414=coordonneesBalle414[1]

        coordonneesBalle415=monCanevas.bbox(balle415)
        x415=coordonneesBalle415[0]
        y415=coordonneesBalle415[1]

        coordonneesBalle416=monCanevas.bbox(balle416)
        x416=coordonneesBalle416[0]
        y416=coordonneesBalle416[1]

        coordonneesBalle417=monCanevas.bbox(balle417)
        x417=coordonneesBalle417[0]
        y417=coordonneesBalle417[1]

        coordonneesBalle418=monCanevas.bbox(balle418)
        x418=coordonneesBalle418[0]
        y418=coordonneesBalle418[1]

        coordonneesBalle419=monCanevas.bbox(balle419)
        x419=coordonneesBalle419[0]
        y419=coordonneesBalle419[1]

        coordonneesBalle420=monCanevas.bbox(balle420)
        x420=coordonneesBalle420[0]
        y420=coordonneesBalle420[1]

        coordonneesBalle421=monCanevas.bbox(balle421)
        x421=coordonneesBalle421[0]
        y421=coordonneesBalle421[1]

        coordonneesBalle422=monCanevas.bbox(balle422)
        x422=coordonneesBalle422[0]
        y422=coordonneesBalle422[1]

        coordonneesBalle423=monCanevas.bbox(balle423)
        x423=coordonneesBalle423[0]
        y423=coordonneesBalle423[1]

        coordonneesBalle424=monCanevas.bbox(balle424)
        x424=coordonneesBalle424[0]
        y424=coordonneesBalle424[1]

        coordonneesBalle425=monCanevas.bbox(balle425)
        x425=coordonneesBalle425[0]
        y425=coordonneesBalle425[1]

        coordonneesBalle426=monCanevas.bbox(balle426)
        x426=coordonneesBalle426[0]
        y426=coordonneesBalle426[1]

        coordonneesBalle427=monCanevas.bbox(balle427)
        x427=coordonneesBalle427[0]
        y427=coordonneesBalle427[1]

        coordonneesBalle428=monCanevas.bbox(balle428)
        x428=coordonneesBalle428[0]
        y428=coordonneesBalle428[1]

        coordonneesBalle429=monCanevas.bbox(balle429)
        x429=coordonneesBalle429[0]
        y429=coordonneesBalle429[1]

        coordonneesBalle430=monCanevas.bbox(balle430)
        x430=coordonneesBalle430[0]
        y430=coordonneesBalle430[1]

        coordonneesBalle431=monCanevas.bbox(balle431)
        x431=coordonneesBalle431[0]
        y431=coordonneesBalle431[1]

        coordonneesBalle432=monCanevas.bbox(balle432)
        x432=coordonneesBalle432[0]
        y432=coordonneesBalle432[1]

        coordonneesBalle433=monCanevas.bbox(balle433)
        x433=coordonneesBalle433[0]
        y433=coordonneesBalle433[1]

        coordonneesBalle434=monCanevas.bbox(balle434)
        x434=coordonneesBalle434[0]
        y434=coordonneesBalle434[1]

        coordonneesBalle435=monCanevas.bbox(balle435)
        x435=coordonneesBalle435[0]
        y435=coordonneesBalle435[1]

        coordonneesBalle436=monCanevas.bbox(balle436)
        x436=coordonneesBalle436[0]
        y436=coordonneesBalle436[1]

        coordonneesBalle437=monCanevas.bbox(balle437)
        x437=coordonneesBalle437[0]
        y437=coordonneesBalle437[1]

        coordonneesBalle438=monCanevas.bbox(balle438)
        x438=coordonneesBalle438[0]
        y438=coordonneesBalle438[1]

        coordonneesBalle439=monCanevas.bbox(balle439)
        x439=coordonneesBalle439[0]
        y439=coordonneesBalle439[1]

        coordonneesBalle440=monCanevas.bbox(balle440)
        x440=coordonneesBalle440[0]
        y440=coordonneesBalle440[1]

        coordonneesBalle441=monCanevas.bbox(balle441)
        x441=coordonneesBalle441[0]
        y441=coordonneesBalle441[1]

        coordonneesBalle442=monCanevas.bbox(balle442)
        x442=coordonneesBalle442[0]
        y442=coordonneesBalle442[1]

        coordonneesBalle443=monCanevas.bbox(balle443)
        x443=coordonneesBalle443[0]
        y443=coordonneesBalle443[1]

        coordonneesBalle444=monCanevas.bbox(balle444)
        x444=coordonneesBalle444[0]
        y444=coordonneesBalle444[1]

        coordonneesBalle445=monCanevas.bbox(balle445)
        x445=coordonneesBalle445[0]
        y445=coordonneesBalle445[1]

        coordonneesBalle446=monCanevas.bbox(balle446)
        x446=coordonneesBalle446[0]
        y446=coordonneesBalle446[1]

        coordonneesBalle447=monCanevas.bbox(balle447)
        x447=coordonneesBalle447[0]
        y447=coordonneesBalle447[1]

        coordonneesBalle448=monCanevas.bbox(balle448)
        x448=coordonneesBalle448[0]
        y448=coordonneesBalle448[1]

        coordonneesBalle449=monCanevas.bbox(balle449)
        x449=coordonneesBalle449[0]
        y449=coordonneesBalle449[1]

        coordonneesBalle450=monCanevas.bbox(balle450)
        x450=coordonneesBalle450[0]
        y450=coordonneesBalle450[1]

        coordonneesBalle451=monCanevas.bbox(balle451)
        x451=coordonneesBalle451[0]
        y451=coordonneesBalle451[1]

        coordonneesBalle452=monCanevas.bbox(balle452)
        x452=coordonneesBalle452[0]
        y452=coordonneesBalle452[1]

        coordonneesBalle453=monCanevas.bbox(balle453)
        x453=coordonneesBalle453[0]
        y453=coordonneesBalle453[1]

        coordonneesBalle454=monCanevas.bbox(balle454)
        x454=coordonneesBalle454[0]
        y454=coordonneesBalle454[1]

        coordonneesBalle455=monCanevas.bbox(balle455)
        x455=coordonneesBalle455[0]
        y455=coordonneesBalle455[1]

        coordonneesBalle456=monCanevas.bbox(balle456)
        x456=coordonneesBalle456[0]
        y456=coordonneesBalle456[1]

        coordonneesBalle457=monCanevas.bbox(balle457)
        x457=coordonneesBalle457[0]
        y457=coordonneesBalle457[1]

        coordonneesBalle458=monCanevas.bbox(balle458)
        x458=coordonneesBalle458[0]
        y458=coordonneesBalle458[1]

        coordonneesBalle459=monCanevas.bbox(balle459)
        x459=coordonneesBalle459[0]
        y459=coordonneesBalle459[1]

        coordonneesBalle460=monCanevas.bbox(balle460)
        x460=coordonneesBalle460[0]
        y460=coordonneesBalle460[1]

        coordonneesBalle461=monCanevas.bbox(balle461)
        x461=coordonneesBalle461[0]
        y461=coordonneesBalle461[1]

        coordonneesBalle462=monCanevas.bbox(balle462)
        x462=coordonneesBalle462[0]
        y462=coordonneesBalle462[1]

        coordonneesBalle463=monCanevas.bbox(balle463)
        x463=coordonneesBalle463[0]
        y463=coordonneesBalle463[1]

        coordonneesBalle464=monCanevas.bbox(balle464)
        x464=coordonneesBalle464[0]
        y464=coordonneesBalle464[1]

        coordonneesBalle465=monCanevas.bbox(balle465)
        x465=coordonneesBalle465[0]
        y465=coordonneesBalle465[1]

        coordonneesBalle466=monCanevas.bbox(balle466)
        x466=coordonneesBalle466[0]
        y466=coordonneesBalle466[1]

        coordonneesBalle467=monCanevas.bbox(balle467)
        x467=coordonneesBalle467[0]
        y467=coordonneesBalle467[1]

        coordonneesBalle468=monCanevas.bbox(balle468)
        x468=coordonneesBalle468[0]
        y468=coordonneesBalle468[1]

        coordonneesBalle469=monCanevas.bbox(balle469)
        x469=coordonneesBalle469[0]
        y469=coordonneesBalle469[1]

        coordonneesBalle470=monCanevas.bbox(balle470)
        x470=coordonneesBalle470[0]
        y470=coordonneesBalle470[1]

        coordonneesBalle471=monCanevas.bbox(balle471)
        x471=coordonneesBalle471[0]
        y471=coordonneesBalle471[1]

        coordonneesBalle472=monCanevas.bbox(balle472)
        x472=coordonneesBalle472[0]
        y472=coordonneesBalle472[1]

        coordonneesBalle473=monCanevas.bbox(balle473)
        x473=coordonneesBalle473[0]
        y473=coordonneesBalle473[1]

        coordonneesBalle474=monCanevas.bbox(balle474)
        x474=coordonneesBalle474[0]
        y474=coordonneesBalle474[1]

        coordonneesBalle475=monCanevas.bbox(balle475)
        x475=coordonneesBalle475[0]
        y475=coordonneesBalle475[1]

        coordonneesBalle476=monCanevas.bbox(balle476)
        x476=coordonneesBalle476[0]
        y476=coordonneesBalle476[1]

        coordonneesBalle477=monCanevas.bbox(balle477)
        x477=coordonneesBalle477[0]
        y477=coordonneesBalle477[1]

        coordonneesBalle478=monCanevas.bbox(balle478)
        x478=coordonneesBalle478[0]
        y478=coordonneesBalle478[1]

        coordonneesBalle479=monCanevas.bbox(balle479)
        x479=coordonneesBalle479[0]
        y479=coordonneesBalle479[1]

        coordonneesBalle480=monCanevas.bbox(balle480)
        x480=coordonneesBalle480[0]
        y480=coordonneesBalle480[1]

        coordonneesBalle481=monCanevas.bbox(balle481)
        x481=coordonneesBalle481[0]
        y481=coordonneesBalle481[1]

        coordonneesBalle482=monCanevas.bbox(balle482)
        x482=coordonneesBalle482[0]
        y482=coordonneesBalle482[1]

        coordonneesBalle483=monCanevas.bbox(balle483)
        x483=coordonneesBalle483[0]
        y483=coordonneesBalle483[1]

        coordonneesBalle484=monCanevas.bbox(balle484)
        x484=coordonneesBalle484[0]
        y484=coordonneesBalle484[1]
        #definition de la mort quand le joueur touche le bord
        dx,dy=testBords(x,y,dx,dy)

        #application du mouvement de la tete
        monCanevas.move(balle,dx,dy)


        #definition et aplication du mouvement des autres carré

        #les 4 carrés de base
        if dd2>-80000 :
            monCanevas.move(balle1,dx1,dy1)
            dx2bis=dx1
            dy2bis=dy1
            dd1=1
        if dd2>-1800 :
            monCanevas.move(balle2,dx2,dy2)
            dx3bis=dx2
            dy3bis=dy2
        if dd2>=-8000 :
            monCanevas.move(balle3,dx3,dy3)
            dx4bis=dx3
            dy4bis=dy3
        if dd2>=-8000 :
            monCanevas.move(balle4,dx4,dy4)
            dx5bis=dx4
            dy5bis=dy4

        #les carés qui dépendent du nombre de pommes

        monCanevas.move(balle5,dx5,dy5)
        dx6bis=dx5
        dy6bis=dy5
        if dd2==1 and dlol==0 :
            monCanevas.move(balle5,-8000,-8000)
            dlol=1


        monCanevas.move(balle6,dx6,dy6)
        dx7bis=dx6
        dy7bis=dy6
        if dd2==2 and dlol==1 :
            monCanevas.move(balle6,-8000,-8000)
            dlol=2


        monCanevas.move(balle7,dx7,dy7)
        dx8bis=dx7
        dy8bis=dy7
        if dd2==3 and dlol==2 :
            monCanevas.move(balle7,-8000,-8000)
            dlol=3

        monCanevas.move(balle8,dx8,dy8)
        dx9bis=dx8
        dy9bis=dy8
        if dd2==4 and dlol==3 :
            monCanevas.move(balle8,-8000,-8000)
            dlol=4

        monCanevas.move(balle9,dx9,dy9)
        dx10bis=dx9
        dy10bis=dy9
        if dd2==5 and dlol==4 :
            monCanevas.move(balle9,-8000,-8000)
            dlol=5

        monCanevas.move(balle10,dx10,dy10)
        dx11bis=dx10
        dy11bis=dy10
        if dd2==6 and dlol==5 :
            monCanevas.move(balle10,-8000,-8000)
            dlol=6

        monCanevas.move(balle11,dx11,dy11)
        dx12bis=dx11
        dy12bis=dy11
        if dd2==7 and dlol==6 :
            monCanevas.move(balle11,-8000,-8000)
            dlol=7

        monCanevas.move(balle12,dx12,dy12)
        dx13bis=dx12
        dy13bis=dy12
        if dd2==8 and dlol==7 :
            monCanevas.move(balle12,-8000,-8000)
            dlol=8

        monCanevas.move(balle13,dx13,dy13)
        dx14bis=dx13
        dy14bis=dy13
        if dd2==9 and dlol==8 :
            monCanevas.move(balle13,-8000,-8000)
            dlol=9

        monCanevas.move(balle14,dx14,dy14)
        dx15bis=dx14
        dy15bis=dy14
        if dd2==10 and dlol==9 :
            monCanevas.move(balle14,-8000,-8000)
            dlol=10

        monCanevas.move(balle15,dx15,dy15)
        dx16bis=dx15
        dy16bis=dy15
        if dd2==11 and dlol==10 :
            monCanevas.move(balle15,-8000,-8000)
            dlol=11

        monCanevas.move(balle16,dx16,dy16)
        dx17bis=dx16
        dy17bis=dy16
        if dd2==12 and dlol==11 :
            monCanevas.move(balle16,-8000,-8000)
            dlol=12

        monCanevas.move(balle17,dx17,dy17)
        dx18bis=dx17
        dy18bis=dy17
        if dd2==13 and dlol==12 :
            monCanevas.move(balle17,-8000,-8000)
            dlol=13

        monCanevas.move(balle18,dx18,dy18)
        dx19bis=dx18
        dy19bis=dy18
        if dd2==14 and dlol==13 :
            monCanevas.move(balle18,-8000,-8000)
            dlol=14

        monCanevas.move(balle19,dx19,dy19)
        dx20bis=dx19
        dy20bis=dy19
        if dd2==15 and dlol==14 :
            monCanevas.move(balle19,-8000,-8000)
            dlol=15

        monCanevas.move(balle20,dx20,dy20)
        dx21bis=dx20
        dy21bis=dy20
        if dd2==16 and dlol==15 :
            monCanevas.move(balle20,-8000,-8000)
            dlol=16

        monCanevas.move(balle21,dx21,dy21)
        dx22bis=dx21
        dy22bis=dy21
        if dd2==17 and dlol==16 :
            monCanevas.move(balle21,-8000,-8000)
            dlol=17

        monCanevas.move(balle22,dx22,dy22)
        dx23bis=dx22
        dy23bis=dy22
        if dd2==18 and dlol==17 :
            monCanevas.move(balle22,-8000,-8000)
            dlol=18

        monCanevas.move(balle23,dx23,dy23)
        dx24bis=dx23
        dy24bis=dy23
        if dd2==19 and dlol==18 :
            monCanevas.move(balle23,-8000,-8000)
            dlol=19

        monCanevas.move(balle24,dx24,dy24)
        dx25bis=dx24
        dy25bis=dy24
        if dd2==20 and dlol==19 :
            monCanevas.move(balle24,-8000,-8000)
            dlol=20

        monCanevas.move(balle25,dx25,dy25)
        dx26bis=dx25
        dy26bis=dy25
        if dd2==21 and dlol==20 :
            monCanevas.move(balle25,-8000,-8000)
            dlol=21

        monCanevas.move(balle26,dx26,dy26)
        dx27bis=dx26
        dy27bis=dy26
        if dd2==22 and dlol==21 :
            monCanevas.move(balle26,-8000,-8000)
            dlol=22

        monCanevas.move(balle27,dx27,dy27)
        dx28bis=dx27
        dy28bis=dy27
        if dd2==23 and dlol==22 :
            monCanevas.move(balle27,-8000,-8000)
            dlol=23

        monCanevas.move(balle28,dx28,dy28)
        dx29bis=dx28
        dy29bis=dy28
        if dd2==24 and dlol==23 :
            monCanevas.move(balle28,-8000,-8000)
            dlol=24

        monCanevas.move(balle29,dx29,dy29)
        dx30bis=dx29
        dy30bis=dy29
        if dd2==25 and dlol==24 :
            monCanevas.move(balle29,-8000,-8000)
            dlol=25

        monCanevas.move(balle30,dx30,dy30)
        dx31bis=dx30
        dy31bis=dy30
        if dd2==26 and dlol==25 :
            monCanevas.move(balle30,-8000,-8000)
            dlol=26

        monCanevas.move(balle31,dx31,dy31)
        dx32bis=dx31
        dy32bis=dy31
        if dd2==27 and dlol==26 :
            monCanevas.move(balle31,-8000,-8000)
            dlol=27

        monCanevas.move(balle32,dx32,dy32)
        dx33bis=dx32
        dy33bis=dy32
        if dd2==28 and dlol==27 :
            monCanevas.move(balle32,-8000,-8000)
            dlol=28

        monCanevas.move(balle33,dx33,dy33)
        dx34bis=dx33
        dy34bis=dy33
        if dd2==29 and dlol==28 :
            monCanevas.move(balle33,-8000,-8000)
            dlol=29

        monCanevas.move(balle34,dx34,dy34)
        dx35bis=dx34
        dy35bis=dy34
        if dd2==30 and dlol==29 :
            monCanevas.move(balle34,-8000,-8000)
            dlol=30

        monCanevas.move(balle35,dx35,dy35)
        dx36bis=dx35
        dy36bis=dy35
        if dd2==31 and dlol==30 :
            monCanevas.move(balle35,-8000,-8000)
            dlol=31

        monCanevas.move(balle36,dx36,dy36)
        dx37bis=dx36
        dy37bis=dy36
        if dd2==32 and dlol==31 :
            monCanevas.move(balle36,-8000,-8000)
            dlol=32

        monCanevas.move(balle37,dx37,dy37)
        dx38bis=dx37
        dy38bis=dy37
        if dd2==33 and dlol==32 :
            monCanevas.move(balle37,-8000,-8000)
            dlol=33

        monCanevas.move(balle38,dx38,dy38)
        dx39bis=dx38
        dy39bis=dy38
        if dd2==34 and dlol==33 :
            monCanevas.move(balle38,-8000,-8000)
            dlol=34

        monCanevas.move(balle39,dx39,dy39)
        dx40bis=dx39
        dy40bis=dy39
        if dd2==35 and dlol==34 :
            monCanevas.move(balle39,-8000,-8000)
            dlol=35

        monCanevas.move(balle40,dx40,dy40)
        dx41bis=dx40
        dy41bis=dy40
        if dd2==36 and dlol==35 :
            monCanevas.move(balle40,-8000,-8000)
            dlol=36

        monCanevas.move(balle41,dx41,dy41)
        dx42bis=dx41
        dy42bis=dy41
        if dd2==37 and dlol==36 :
            monCanevas.move(balle41,-8000,-8000)
            dlol=37

        monCanevas.move(balle42,dx42,dy42)
        dx43bis=dx42
        dy43bis=dy42
        if dd2==38 and dlol==37 :
            monCanevas.move(balle42,-8000,-8000)
            dlol=38

        monCanevas.move(balle43,dx43,dy43)
        dx44bis=dx43
        dy44bis=dy43
        if dd2==39 and dlol==38 :
            monCanevas.move(balle43,-8000,-8000)
            dlol=39

        monCanevas.move(balle44,dx44,dy44)
        dx45bis=dx44
        dy45bis=dy44
        if dd2==40 and dlol==39 :
            monCanevas.move(balle44,-8000,-8000)
            dlol=40

        monCanevas.move(balle45,dx45,dy45)
        dx46bis=dx45
        dy46bis=dy45
        if dd2==41 and dlol==40 :
            monCanevas.move(balle45,-8000,-8000)
            dlol=41

        monCanevas.move(balle46,dx46,dy46)
        dx47bis=dx46
        dy47bis=dy46
        if dd2==42 and dlol==41 :
            monCanevas.move(balle46,-8000,-8000)
            dlol=42

        monCanevas.move(balle47,dx47,dy47)
        dx48bis=dx47
        dy48bis=dy47
        if dd2==43 and dlol==42 :
            monCanevas.move(balle47,-8000,-8000)
            dlol=43

        monCanevas.move(balle48,dx48,dy48)
        dx49bis=dx48
        dy49bis=dy48
        if dd2==44 and dlol==43 :
            monCanevas.move(balle48,-8000,-8000)
            dlol=44

        monCanevas.move(balle49,dx49,dy49)
        dx50bis=dx49
        dy50bis=dy49
        if dd2==45 and dlol==44 :
            monCanevas.move(balle49,-8000,-8000)
            dlol=45

        monCanevas.move(balle50,dx50,dy50)
        dx51bis=dx50
        dy51bis=dy50
        if dd2==46 and dlol==45 :
            monCanevas.move(balle50,-8000,-8000)
            dlol=46

        monCanevas.move(balle51,dx51,dy51)
        dx52bis=dx51
        dy52bis=dy51
        if dd2==47 and dlol==46 :
            monCanevas.move(balle51,-8000,-8000)
            dlol=47

        monCanevas.move(balle52,dx52,dy52)
        dx53bis=dx52
        dy53bis=dy52
        if dd2==48 and dlol==47 :
            monCanevas.move(balle52,-8000,-8000)
            dlol=48

        monCanevas.move(balle53,dx53,dy53)
        dx54bis=dx53
        dy54bis=dy53
        if dd2==49 and dlol==48 :
            monCanevas.move(balle53,-8000,-8000)
            dlol=49

        monCanevas.move(balle54,dx54,dy54)
        dx55bis=dx54
        dy55bis=dy54
        if dd2==50 and dlol==49 :
            monCanevas.move(balle54,-8000,-8000)
            dlol=50

        monCanevas.move(balle55,dx55,dy55)
        dx56bis=dx55
        dy56bis=dy55
        if dd2==51 and dlol==50 :
            monCanevas.move(balle55,-8000,-8000)
            dlol=51

        monCanevas.move(balle56,dx56,dy56)
        dx57bis=dx56
        dy57bis=dy56
        if dd2==52 and dlol==51 :
            monCanevas.move(balle56,-8000,-8000)
            dlol=52

        monCanevas.move(balle57,dx57,dy57)
        dx58bis=dx57
        dy58bis=dy57
        if dd2==53 and dlol==52 :
            monCanevas.move(balle57,-8000,-8000)
            dlol=53

        monCanevas.move(balle58,dx58,dy58)
        dx59bis=dx58
        dy59bis=dy58
        if dd2==54 and dlol==53 :
            monCanevas.move(balle58,-8000,-8000)
            dlol=54

        monCanevas.move(balle59,dx59,dy59)
        dx60bis=dx59
        dy60bis=dy59
        if dd2==55 and dlol==54 :
            monCanevas.move(balle59,-8000,-8000)
            dlol=55

        monCanevas.move(balle60,dx60,dy60)
        dx61bis=dx60
        dy61bis=dy60
        if dd2==56 and dlol==55 :
            monCanevas.move(balle60,-8000,-8000)
            dlol=56

        monCanevas.move(balle61,dx61,dy61)
        dx62bis=dx61
        dy62bis=dy61
        if dd2==57 and dlol==56 :
            monCanevas.move(balle61,-8000,-8000)
            dlol=57

        monCanevas.move(balle62,dx62,dy62)
        dx63bis=dx62
        dy63bis=dy62
        if dd2==58 and dlol==57 :
            monCanevas.move(balle62,-8000,-8000)
            dlol=58

        monCanevas.move(balle63,dx63,dy63)
        dx64bis=dx63
        dy64bis=dy63
        if dd2==59 and dlol==58 :
            monCanevas.move(balle63,-8000,-8000)
            dlol=59

        monCanevas.move(balle64,dx64,dy64)
        dx65bis=dx64
        dy65bis=dy64
        if dd2==60 and dlol==59 :
            monCanevas.move(balle64,-8000,-8000)
            dlol=60

        monCanevas.move(balle65,dx65,dy65)
        dx66bis=dx65
        dy66bis=dy65
        if dd2==61 and dlol==60 :
            monCanevas.move(balle65,-8000,-8000)
            dlol=61

        monCanevas.move(balle66,dx66,dy66)
        dx67bis=dx66
        dy67bis=dy66
        if dd2==62 and dlol==61 :
            monCanevas.move(balle66,-8000,-8000)
            dlol=62

        monCanevas.move(balle67,dx67,dy67)
        dx68bis=dx67
        dy68bis=dy67
        if dd2==63 and dlol==62 :
            monCanevas.move(balle67,-8000,-8000)
            dlol=63

        monCanevas.move(balle68,dx68,dy68)
        dx69bis=dx68
        dy69bis=dy68
        if dd2==64 and dlol==63 :
            monCanevas.move(balle68,-8000,-8000)
            dlol=64

        monCanevas.move(balle69,dx69,dy69)
        dx70bis=dx69
        dy70bis=dy69
        if dd2==65 and dlol==64 :
            monCanevas.move(balle69,-8000,-8000)
            dlol=65

        monCanevas.move(balle70,dx70,dy70)
        dx71bis=dx70
        dy71bis=dy70
        if dd2==66 and dlol==65 :
            monCanevas.move(balle70,-8000,-8000)
            dlol=66

        monCanevas.move(balle71,dx71,dy71)
        dx72bis=dx71
        dy72bis=dy71
        if dd2==67 and dlol==66 :
            monCanevas.move(balle71,-8000,-8000)
            dlol=67

        monCanevas.move(balle72,dx72,dy72)
        dx73bis=dx72
        dy73bis=dy72
        if dd2==68 and dlol==67 :
            monCanevas.move(balle72,-8000,-8000)
            dlol=68

        monCanevas.move(balle73,dx73,dy73)
        dx74bis=dx73
        dy74bis=dy73
        if dd2==69 and dlol==68 :
            monCanevas.move(balle73,-8000,-8000)
            dlol=69

        monCanevas.move(balle74,dx74,dy74)
        dx75bis=dx74
        dy75bis=dy74
        if dd2==70 and dlol==69 :
            monCanevas.move(balle74,-8000,-8000)
            dlol=70

        monCanevas.move(balle75,dx75,dy75)
        dx76bis=dx75
        dy76bis=dy75
        if dd2==71 and dlol==70 :
            monCanevas.move(balle75,-8000,-8000)
            dlol=71

        monCanevas.move(balle76,dx76,dy76)
        dx77bis=dx76
        dy77bis=dy76
        if dd2==72 and dlol==71 :
            monCanevas.move(balle76,-8000,-8000)
            dlol=72

        monCanevas.move(balle77,dx77,dy77)
        dx78bis=dx77
        dy78bis=dy77
        if dd2==73 and dlol==72 :
            monCanevas.move(balle77,-8000,-8000)
            dlol=73

        monCanevas.move(balle78,dx78,dy78)
        dx79bis=dx78
        dy79bis=dy78
        if dd2==74 and dlol==73 :
            monCanevas.move(balle78,-8000,-8000)
            dlol=74

        monCanevas.move(balle79,dx79,dy79)
        dx80bis=dx79
        dy80bis=dy79
        if dd2==75 and dlol==74 :
            monCanevas.move(balle79,-8000,-8000)
            dlol=75

        monCanevas.move(balle80,dx80,dy80)
        dx81bis=dx80
        dy81bis=dy80
        if dd2==76 and dlol==75 :
            monCanevas.move(balle80,-8000,-8000)
            dlol=76

        monCanevas.move(balle81,dx81,dy81)
        dx82bis=dx81
        dy82bis=dy81
        if dd2==77 and dlol==76 :
            monCanevas.move(balle81,-8000,-8000)
            dlol=77

        monCanevas.move(balle82,dx82,dy82)
        dx83bis=dx82
        dy83bis=dy82
        if dd2==78 and dlol==77 :
            monCanevas.move(balle82,-8000,-8000)
            dlol=78

        monCanevas.move(balle83,dx83,dy83)
        dx84bis=dx83
        dy84bis=dy83
        if dd2==79 and dlol==78 :
            monCanevas.move(balle83,-8000,-8000)
            dlol=79

        monCanevas.move(balle84,dx84,dy84)
        dx85bis=dx84
        dy85bis=dy84
        if dd2==80 and dlol==79 :
            monCanevas.move(balle84,-8000,-8000)
            dlol=80

        monCanevas.move(balle85,dx85,dy85)
        dx86bis=dx85
        dy86bis=dy85
        if dd2==81 and dlol==80 :
            monCanevas.move(balle85,-8000,-8000)
            dlol=81

        monCanevas.move(balle86,dx86,dy86)
        dx87bis=dx86
        dy87bis=dy86
        if dd2==82 and dlol==81 :
            monCanevas.move(balle86,-8000,-8000)
            dlol=82

        monCanevas.move(balle87,dx87,dy87)
        dx88bis=dx87
        dy88bis=dy87
        if dd2==83 and dlol==82 :
            monCanevas.move(balle87,-8000,-8000)
            dlol=83

        monCanevas.move(balle88,dx88,dy88)
        dx89bis=dx88
        dy89bis=dy88
        if dd2==84 and dlol==83 :
            monCanevas.move(balle88,-8000,-8000)
            dlol=84

        monCanevas.move(balle89,dx89,dy89)
        dx90bis=dx89
        dy90bis=dy89
        if dd2==85 and dlol==84 :
            monCanevas.move(balle89,-8000,-8000)
            dlol=85

        monCanevas.move(balle90,dx90,dy90)
        dx91bis=dx90
        dy91bis=dy90
        if dd2==86 and dlol==85 :
            monCanevas.move(balle90,-8000,-8000)
            dlol=86

        monCanevas.move(balle91,dx91,dy91)
        dx92bis=dx91
        dy92bis=dy91
        if dd2==87 and dlol==86 :
            monCanevas.move(balle91,-8000,-8000)
            dlol=87

        monCanevas.move(balle92,dx92,dy92)
        dx93bis=dx92
        dy93bis=dy92
        if dd2==88 and dlol==87 :
            monCanevas.move(balle92,-8000,-8000)
            dlol=88

        monCanevas.move(balle93,dx93,dy93)
        dx94bis=dx93
        dy94bis=dy93
        if dd2==89 and dlol==88 :
            monCanevas.move(balle93,-8000,-8000)
            dlol=89

        monCanevas.move(balle94,dx94,dy94)
        dx95bis=dx94
        dy95bis=dy94
        if dd2==90 and dlol==89 :
            monCanevas.move(balle94,-8000,-8000)
            dlol=90

        monCanevas.move(balle95,dx95,dy95)
        dx96bis=dx95
        dy96bis=dy95
        if dd2==91 and dlol==90 :
            monCanevas.move(balle95,-8000,-8000)
            dlol=91

        monCanevas.move(balle96,dx96,dy96)
        dx97bis=dx96
        dy97bis=dy96
        if dd2==92 and dlol==91 :
            monCanevas.move(balle96,-8000,-8000)
            dlol=92

        monCanevas.move(balle97,dx97,dy97)
        dx98bis=dx97
        dy98bis=dy97
        if dd2==93 and dlol==92 :
            monCanevas.move(balle97,-8000,-8000)
            dlol=93

        monCanevas.move(balle98,dx98,dy98)
        dx99bis=dx98
        dy99bis=dy98
        if dd2==94 and dlol==93 :
            monCanevas.move(balle98,-8000,-8000)
            dlol=94

        monCanevas.move(balle99,dx99,dy99)
        dx100bis=dx99
        dy100bis=dy99
        if dd2==95 and dlol==94 :
            monCanevas.move(balle99,-8000,-8000)
            dlol=95

        monCanevas.move(balle100,dx100,dy100)
        dx101bis=dx100
        dy101bis=dy100
        if dd2==96 and dlol==95 :
            monCanevas.move(balle100,-8000,-8000)
            dlol=96

        monCanevas.move(balle101,dx101,dy101)
        dx102bis=dx101
        dy102bis=dy101
        if dd2==97 and dlol==96 :
            monCanevas.move(balle101,-8000,-8000)
            dlol=97

        monCanevas.move(balle102,dx102,dy102)
        dx103bis=dx102
        dy103bis=dy102
        if dd2==98 and dlol==97 :
            monCanevas.move(balle102,-8000,-8000)
            dlol=98

        monCanevas.move(balle103,dx103,dy103)
        dx104bis=dx103
        dy104bis=dy103
        if dd2==99 and dlol==98 :
            monCanevas.move(balle103,-8000,-8000)
            dlol=99

        monCanevas.move(balle104,dx104,dy104)
        dx105bis=dx104
        dy105bis=dy104
        if dd2==100 and dlol==99 :
            monCanevas.move(balle104,-8000,-8000)
            dlol=100

        monCanevas.move(balle105,dx105,dy105)
        dx106bis=dx105
        dy106bis=dy105
        if dd2==101 and dlol==100 :
            monCanevas.move(balle105,-8000,-8000)
            dlol=101

        monCanevas.move(balle106,dx106,dy106)
        dx107bis=dx106
        dy107bis=dy106
        if dd2==102 and dlol==101 :
            monCanevas.move(balle106,-8000,-8000)
            dlol=102

        monCanevas.move(balle107,dx107,dy107)
        dx108bis=dx107
        dy108bis=dy107
        if dd2==103 and dlol==102 :
            monCanevas.move(balle107,-8000,-8000)
            dlol=103

        monCanevas.move(balle108,dx108,dy108)
        dx109bis=dx108
        dy109bis=dy108
        if dd2==104 and dlol==103 :
            monCanevas.move(balle108,-8000,-8000)
            dlol=104

        monCanevas.move(balle109,dx109,dy109)
        dx110bis=dx109
        dy110bis=dy109
        if dd2==105 and dlol==104 :
            monCanevas.move(balle109,-8000,-8000)
            dlol=105

        monCanevas.move(balle110,dx110,dy110)
        dx111bis=dx110
        dy111bis=dy110
        if dd2==106 and dlol==105 :
            monCanevas.move(balle110,-8000,-8000)
            dlol=106

        monCanevas.move(balle111,dx111,dy111)
        dx112bis=dx111
        dy112bis=dy111
        if dd2==107 and dlol==106 :
            monCanevas.move(balle111,-8000,-8000)
            dlol=107

        monCanevas.move(balle112,dx112,dy112)
        dx113bis=dx112
        dy113bis=dy112
        if dd2==108 and dlol==107 :
            monCanevas.move(balle112,-8000,-8000)
            dlol=108

        monCanevas.move(balle113,dx113,dy113)
        dx114bis=dx113
        dy114bis=dy113
        if dd2==109 and dlol==108 :
            monCanevas.move(balle113,-8000,-8000)
            dlol=109

        monCanevas.move(balle114,dx114,dy114)
        dx115bis=dx114
        dy115bis=dy114
        if dd2==110 and dlol==109 :
            monCanevas.move(balle114,-8000,-8000)
            dlol=110

        monCanevas.move(balle115,dx115,dy115)
        dx116bis=dx115
        dy116bis=dy115
        if dd2==111 and dlol==110 :
            monCanevas.move(balle115,-8000,-8000)
            dlol=111

        monCanevas.move(balle116,dx116,dy116)
        dx117bis=dx116
        dy117bis=dy116
        if dd2==112 and dlol==111 :
            monCanevas.move(balle116,-8000,-8000)
            dlol=112

        monCanevas.move(balle117,dx117,dy117)
        dx118bis=dx117
        dy118bis=dy117
        if dd2==113 and dlol==112 :
            monCanevas.move(balle117,-8000,-8000)
            dlol=113

        monCanevas.move(balle118,dx118,dy118)
        dx119bis=dx118
        dy119bis=dy118
        if dd2==114 and dlol==113 :
            monCanevas.move(balle118,-8000,-8000)
            dlol=114

        monCanevas.move(balle119,dx119,dy119)
        dx120bis=dx119
        dy120bis=dy119
        if dd2==115 and dlol==114 :
            monCanevas.move(balle119,-8000,-8000)
            dlol=115

        monCanevas.move(balle120,dx120,dy120)
        dx121bis=dx120
        dy121bis=dy120
        if dd2==116 and dlol==115 :
            monCanevas.move(balle120,-8000,-8000)
            dlol=116

        monCanevas.move(balle121,dx121,dy121)
        dx122bis=dx121
        dy122bis=dy121
        if dd2==117 and dlol==116 :
            monCanevas.move(balle121,-8000,-8000)
            dlol=117

        monCanevas.move(balle122,dx122,dy122)
        dx123bis=dx122
        dy123bis=dy122
        if dd2==118 and dlol==117 :
            monCanevas.move(balle122,-8000,-8000)
            dlol=118

        monCanevas.move(balle123,dx123,dy123)
        dx124bis=dx123
        dy124bis=dy123
        if dd2==119 and dlol==118 :
            monCanevas.move(balle123,-8000,-8000)
            dlol=119

        monCanevas.move(balle124,dx124,dy124)
        dx125bis=dx124
        dy125bis=dy124
        if dd2==120 and dlol==119 :
            monCanevas.move(balle124,-8000,-8000)
            dlol=120

        monCanevas.move(balle125,dx125,dy125)
        dx126bis=dx125
        dy126bis=dy125
        if dd2==121 and dlol==120 :
            monCanevas.move(balle125,-8000,-8000)
            dlol=121

        monCanevas.move(balle126,dx126,dy126)
        dx127bis=dx126
        dy127bis=dy126
        if dd2==122 and dlol==121 :
            monCanevas.move(balle126,-8000,-8000)
            dlol=122

        monCanevas.move(balle127,dx127,dy127)
        dx128bis=dx127
        dy128bis=dy127
        if dd2==123 and dlol==122 :
            monCanevas.move(balle127,-8000,-8000)
            dlol=123

        monCanevas.move(balle128,dx128,dy128)
        dx129bis=dx128
        dy129bis=dy128
        if dd2==124 and dlol==123 :
            monCanevas.move(balle128,-8000,-8000)
            dlol=124

        monCanevas.move(balle129,dx129,dy129)
        dx130bis=dx129
        dy130bis=dy129
        if dd2==125 and dlol==124 :
            monCanevas.move(balle129,-8000,-8000)
            dlol=125

        monCanevas.move(balle130,dx130,dy130)
        dx131bis=dx130
        dy131bis=dy130
        if dd2==126 and dlol==125 :
            monCanevas.move(balle130,-8000,-8000)
            dlol=126

        monCanevas.move(balle131,dx131,dy131)
        dx132bis=dx131
        dy132bis=dy131
        if dd2==127 and dlol==126 :
            monCanevas.move(balle131,-8000,-8000)
            dlol=127

        monCanevas.move(balle132,dx132,dy132)
        dx133bis=dx132
        dy133bis=dy132
        if dd2==128 and dlol==127 :
            monCanevas.move(balle132,-8000,-8000)
            dlol=128

        monCanevas.move(balle133,dx133,dy133)
        dx134bis=dx133
        dy134bis=dy133
        if dd2==129 and dlol==128 :
            monCanevas.move(balle133,-8000,-8000)
            dlol=129

        monCanevas.move(balle134,dx134,dy134)
        dx135bis=dx134
        dy135bis=dy134
        if dd2==130 and dlol==129 :
            monCanevas.move(balle134,-8000,-8000)
            dlol=130

        monCanevas.move(balle135,dx135,dy135)
        dx136bis=dx135
        dy136bis=dy135
        if dd2==131 and dlol==130 :
            monCanevas.move(balle135,-8000,-8000)
            dlol=131

        monCanevas.move(balle136,dx136,dy136)
        dx137bis=dx136
        dy137bis=dy136
        if dd2==132 and dlol==131 :
            monCanevas.move(balle136,-8000,-8000)
            dlol=132

        monCanevas.move(balle137,dx137,dy137)
        dx138bis=dx137
        dy138bis=dy137
        if dd2==133 and dlol==132 :
            monCanevas.move(balle137,-8000,-8000)
            dlol=133

        monCanevas.move(balle138,dx138,dy138)
        dx139bis=dx138
        dy139bis=dy138
        if dd2==134 and dlol==133 :
            monCanevas.move(balle138,-8000,-8000)
            dlol=134

        monCanevas.move(balle139,dx139,dy139)
        dx140bis=dx139
        dy140bis=dy139
        if dd2==135 and dlol==134 :
            monCanevas.move(balle139,-8000,-8000)
            dlol=135

        monCanevas.move(balle140,dx140,dy140)
        dx141bis=dx140
        dy141bis=dy140
        if dd2==136 and dlol==135 :
            monCanevas.move(balle140,-8000,-8000)
            dlol=136

        monCanevas.move(balle141,dx141,dy141)
        dx142bis=dx141
        dy142bis=dy141
        if dd2==137 and dlol==136 :
            monCanevas.move(balle141,-8000,-8000)
            dlol=137

        monCanevas.move(balle142,dx142,dy142)
        dx143bis=dx142
        dy143bis=dy142
        if dd2==138 and dlol==137 :
            monCanevas.move(balle142,-8000,-8000)
            dlol=138

        monCanevas.move(balle143,dx143,dy143)
        dx144bis=dx143
        dy144bis=dy143
        if dd2==139 and dlol==138 :
            monCanevas.move(balle143,-8000,-8000)
            dlol=139

        monCanevas.move(balle144,dx144,dy144)
        dx145bis=dx144
        dy145bis=dy144
        if dd2==140 and dlol==139 :
            monCanevas.move(balle144,-8000,-8000)
            dlol=140

        monCanevas.move(balle145,dx145,dy145)
        dx146bis=dx145
        dy146bis=dy145
        if dd2==141 and dlol==140 :
            monCanevas.move(balle145,-8000,-8000)
            dlol=141

        monCanevas.move(balle146,dx146,dy146)
        dx147bis=dx146
        dy147bis=dy146
        if dd2==142 and dlol==141 :
            monCanevas.move(balle146,-8000,-8000)
            dlol=142

        monCanevas.move(balle147,dx147,dy147)
        dx148bis=dx147
        dy148bis=dy147
        if dd2==143 and dlol==142 :
            monCanevas.move(balle147,-8000,-8000)
            dlol=143

        monCanevas.move(balle148,dx148,dy148)
        dx149bis=dx148
        dy149bis=dy148
        if dd2==144 and dlol==143 :
            monCanevas.move(balle148,-8000,-8000)
            dlol=144

        monCanevas.move(balle149,dx149,dy149)
        dx150bis=dx149
        dy150bis=dy149
        if dd2==145 and dlol==144 :
            monCanevas.move(balle149,-8000,-8000)
            dlol=145

        monCanevas.move(balle150,dx150,dy150)
        dx151bis=dx150
        dy151bis=dy150
        if dd2==146 and dlol==145 :
            monCanevas.move(balle150,-8000,-8000)
            dlol=146

        monCanevas.move(balle151,dx151,dy151)
        dx152bis=dx151
        dy152bis=dy151
        if dd2==147 and dlol==146 :
            monCanevas.move(balle151,-8000,-8000)
            dlol=147

        monCanevas.move(balle152,dx152,dy152)
        dx153bis=dx152
        dy153bis=dy152
        if dd2==148 and dlol==147 :
            monCanevas.move(balle152,-8000,-8000)
            dlol=148

        monCanevas.move(balle153,dx153,dy153)
        dx154bis=dx153
        dy154bis=dy153
        if dd2==149 and dlol==148 :
            monCanevas.move(balle153,-8000,-8000)
            dlol=149

        monCanevas.move(balle154,dx154,dy154)
        dx155bis=dx154
        dy155bis=dy154
        if dd2==150 and dlol==149 :
            monCanevas.move(balle154,-8000,-8000)
            dlol=150

        monCanevas.move(balle155,dx155,dy155)
        dx156bis=dx155
        dy156bis=dy155
        if dd2==151 and dlol==150 :
            monCanevas.move(balle155,-8000,-8000)
            dlol=151

        monCanevas.move(balle156,dx156,dy156)
        dx157bis=dx156
        dy157bis=dy156
        if dd2==152 and dlol==151 :
            monCanevas.move(balle156,-8000,-8000)
            dlol=152

        monCanevas.move(balle157,dx157,dy157)
        dx158bis=dx157
        dy158bis=dy157
        if dd2==153 and dlol==152 :
            monCanevas.move(balle157,-8000,-8000)
            dlol=153

        monCanevas.move(balle158,dx158,dy158)
        dx159bis=dx158
        dy159bis=dy158
        if dd2==154 and dlol==153 :
            monCanevas.move(balle158,-8000,-8000)
            dlol=154

        monCanevas.move(balle159,dx159,dy159)
        dx160bis=dx159
        dy160bis=dy159
        if dd2==155 and dlol==154 :
            monCanevas.move(balle159,-8000,-8000)
            dlol=155

        monCanevas.move(balle160,dx160,dy160)
        dx161bis=dx160
        dy161bis=dy160
        if dd2==156 and dlol==155 :
            monCanevas.move(balle160,-8000,-8000)
            dlol=156

        monCanevas.move(balle161,dx161,dy161)
        dx162bis=dx161
        dy162bis=dy161
        if dd2==157 and dlol==156 :
            monCanevas.move(balle161,-8000,-8000)
            dlol=157

        monCanevas.move(balle162,dx162,dy162)
        dx163bis=dx162
        dy163bis=dy162
        if dd2==158 and dlol==157 :
            monCanevas.move(balle162,-8000,-8000)
            dlol=158

        monCanevas.move(balle163,dx163,dy163)
        dx164bis=dx163
        dy164bis=dy163
        if dd2==159 and dlol==158 :
            monCanevas.move(balle163,-8000,-8000)
            dlol=159

        monCanevas.move(balle164,dx164,dy164)
        dx165bis=dx164
        dy165bis=dy164
        if dd2==160 and dlol==159 :
            monCanevas.move(balle164,-8000,-8000)
            dlol=160

        monCanevas.move(balle165,dx165,dy165)
        dx166bis=dx165
        dy166bis=dy165
        if dd2==161 and dlol==160 :
            monCanevas.move(balle165,-8000,-8000)
            dlol=161

        monCanevas.move(balle166,dx166,dy166)
        dx167bis=dx166
        dy167bis=dy166
        if dd2==162 and dlol==161 :
            monCanevas.move(balle166,-8000,-8000)
            dlol=162

        monCanevas.move(balle167,dx167,dy167)
        dx168bis=dx167
        dy168bis=dy167
        if dd2==163 and dlol==162 :
            monCanevas.move(balle167,-8000,-8000)
            dlol=163

        monCanevas.move(balle168,dx168,dy168)
        dx169bis=dx168
        dy169bis=dy168
        if dd2==164 and dlol==163 :
            monCanevas.move(balle168,-8000,-8000)
            dlol=164

        monCanevas.move(balle169,dx169,dy169)
        dx170bis=dx169
        dy170bis=dy169
        if dd2==165 and dlol==164 :
            monCanevas.move(balle169,-8000,-8000)
            dlol=165

        monCanevas.move(balle170,dx170,dy170)
        dx171bis=dx170
        dy171bis=dy170
        if dd2==166 and dlol==165 :
            monCanevas.move(balle170,-8000,-8000)
            dlol=166

        monCanevas.move(balle171,dx171,dy171)
        dx172bis=dx171
        dy172bis=dy171
        if dd2==167 and dlol==166 :
            monCanevas.move(balle171,-8000,-8000)
            dlol=167

        monCanevas.move(balle172,dx172,dy172)
        dx173bis=dx172
        dy173bis=dy172
        if dd2==168 and dlol==167 :
            monCanevas.move(balle172,-8000,-8000)
            dlol=168

        monCanevas.move(balle173,dx173,dy173)
        dx174bis=dx173
        dy174bis=dy173
        if dd2==169 and dlol==168 :
            monCanevas.move(balle173,-8000,-8000)
            dlol=169

        monCanevas.move(balle174,dx174,dy174)
        dx175bis=dx174
        dy175bis=dy174
        if dd2==170 and dlol==169 :
            monCanevas.move(balle174,-8000,-8000)
            dlol=170

        monCanevas.move(balle175,dx175,dy175)
        dx176bis=dx175
        dy176bis=dy175
        if dd2==171 and dlol==170 :
            monCanevas.move(balle175,-8000,-8000)
            dlol=171

        monCanevas.move(balle176,dx176,dy176)
        dx177bis=dx176
        dy177bis=dy176
        if dd2==172 and dlol==171 :
            monCanevas.move(balle176,-8000,-8000)
            dlol=172

        monCanevas.move(balle177,dx177,dy177)
        dx178bis=dx177
        dy178bis=dy177
        if dd2==173 and dlol==172 :
            monCanevas.move(balle177,-8000,-8000)
            dlol=173

        monCanevas.move(balle178,dx178,dy178)
        dx179bis=dx178
        dy179bis=dy178
        if dd2==174 and dlol==173 :
            monCanevas.move(balle178,-8000,-8000)
            dlol=174

        monCanevas.move(balle179,dx179,dy179)
        dx180bis=dx179
        dy180bis=dy179
        if dd2==175 and dlol==174 :
            monCanevas.move(balle179,-8000,-8000)
            dlol=175

        monCanevas.move(balle180,dx180,dy180)
        dx181bis=dx180
        dy181bis=dy180
        if dd2==176 and dlol==175 :
            monCanevas.move(balle180,-8000,-8000)
            dlol=176

        monCanevas.move(balle181,dx181,dy181)
        dx182bis=dx181
        dy182bis=dy181
        if dd2==177 and dlol==176 :
            monCanevas.move(balle181,-8000,-8000)
            dlol=177

        monCanevas.move(balle182,dx182,dy182)
        dx183bis=dx182
        dy183bis=dy182
        if dd2==178 and dlol==177 :
            monCanevas.move(balle182,-8000,-8000)
            dlol=178

        monCanevas.move(balle183,dx183,dy183)
        dx184bis=dx183
        dy184bis=dy183
        if dd2==179 and dlol==178 :
            monCanevas.move(balle183,-8000,-8000)
            dlol=179

        monCanevas.move(balle184,dx184,dy184)
        dx185bis=dx184
        dy185bis=dy184
        if dd2==180 and dlol==179 :
            monCanevas.move(balle184,-8000,-8000)
            dlol=180

        monCanevas.move(balle185,dx185,dy185)
        dx186bis=dx185
        dy186bis=dy185
        if dd2==181 and dlol==180 :
            monCanevas.move(balle185,-8000,-8000)
            dlol=181

        monCanevas.move(balle186,dx186,dy186)
        dx187bis=dx186
        dy187bis=dy186
        if dd2==182 and dlol==181 :
            monCanevas.move(balle186,-8000,-8000)
            dlol=182

        monCanevas.move(balle187,dx187,dy187)
        dx188bis=dx187
        dy188bis=dy187
        if dd2==183 and dlol==182 :
            monCanevas.move(balle187,-8000,-8000)
            dlol=183

        monCanevas.move(balle188,dx188,dy188)
        dx189bis=dx188
        dy189bis=dy188
        if dd2==184 and dlol==183 :
            monCanevas.move(balle188,-8000,-8000)
            dlol=184

        monCanevas.move(balle189,dx189,dy189)
        dx190bis=dx189
        dy190bis=dy189
        if dd2==185 and dlol==184 :
            monCanevas.move(balle189,-8000,-8000)
            dlol=185

        monCanevas.move(balle190,dx190,dy190)
        dx191bis=dx190
        dy191bis=dy190
        if dd2==186 and dlol==185 :
            monCanevas.move(balle190,-8000,-8000)
            dlol=186

        monCanevas.move(balle191,dx191,dy191)
        dx192bis=dx191
        dy192bis=dy191
        if dd2==187 and dlol==186 :
            monCanevas.move(balle191,-8000,-8000)
            dlol=187

        monCanevas.move(balle192,dx192,dy192)
        dx193bis=dx192
        dy193bis=dy192
        if dd2==188 and dlol==187 :
            monCanevas.move(balle192,-8000,-8000)
            dlol=188

        monCanevas.move(balle193,dx193,dy193)
        dx194bis=dx193
        dy194bis=dy193
        if dd2==189 and dlol==188 :
            monCanevas.move(balle193,-8000,-8000)
            dlol=189

        monCanevas.move(balle194,dx194,dy194)
        dx195bis=dx194
        dy195bis=dy194
        if dd2==190 and dlol==189 :
            monCanevas.move(balle194,-8000,-8000)
            dlol=190

        monCanevas.move(balle195,dx195,dy195)
        dx196bis=dx195
        dy196bis=dy195
        if dd2==191 and dlol==190 :
            monCanevas.move(balle195,-8000,-8000)
            dlol=191

        monCanevas.move(balle196,dx196,dy196)
        dx197bis=dx196
        dy197bis=dy196
        if dd2==192 and dlol==191 :
            monCanevas.move(balle196,-8000,-8000)
            dlol=192

        monCanevas.move(balle197,dx197,dy197)
        dx198bis=dx197
        dy198bis=dy197
        if dd2==193 and dlol==192 :
            monCanevas.move(balle197,-8000,-8000)
            dlol=193

        monCanevas.move(balle198,dx198,dy198)
        dx199bis=dx198
        dy199bis=dy198
        if dd2==194 and dlol==193 :
            monCanevas.move(balle198,-8000,-8000)
            dlol=194

        monCanevas.move(balle199,dx199,dy199)
        dx200bis=dx199
        dy200bis=dy199
        if dd2==195 and dlol==194 :
            monCanevas.move(balle199,-8000,-8000)
            dlol=195

        monCanevas.move(balle200,dx200,dy200)
        dx201bis=dx200
        dy201bis=dy200
        if dd2==196 and dlol==195 :
            monCanevas.move(balle200,-8000,-8000)
            dlol=196

        monCanevas.move(balle201,dx201,dy201)
        dx202bis=dx201
        dy202bis=dy201
        if dd2==197 and dlol==196 :
            monCanevas.move(balle201,-8000,-8000)
            dlol=197

        monCanevas.move(balle202,dx202,dy202)
        dx203bis=dx202
        dy203bis=dy202
        if dd2==198 and dlol==197 :
            monCanevas.move(balle202,-8000,-8000)
            dlol=198

        monCanevas.move(balle203,dx203,dy203)
        dx204bis=dx203
        dy204bis=dy203
        if dd2==199 and dlol==198 :
            monCanevas.move(balle203,-8000,-8000)
            dlol=199

        monCanevas.move(balle204,dx204,dy204)
        dx205bis=dx204
        dy205bis=dy204
        if dd2==200 and dlol==199 :
            monCanevas.move(balle204,-8000,-8000)
            dlol=200

        monCanevas.move(balle205,dx205,dy205)
        dx206bis=dx205
        dy206bis=dy205
        if dd2==201 and dlol==200 :
            monCanevas.move(balle205,-8000,-8000)
            dlol=201

        monCanevas.move(balle206,dx206,dy206)
        dx207bis=dx206
        dy207bis=dy206
        if dd2==202 and dlol==201 :
            monCanevas.move(balle206,-8000,-8000)
            dlol=202

        monCanevas.move(balle207,dx207,dy207)
        dx208bis=dx207
        dy208bis=dy207
        if dd2==203 and dlol==202 :
            monCanevas.move(balle207,-8000,-8000)
            dlol=203

        monCanevas.move(balle208,dx208,dy208)
        dx209bis=dx208
        dy209bis=dy208
        if dd2==204 and dlol==203 :
            monCanevas.move(balle208,-8000,-8000)
            dlol=204

        monCanevas.move(balle209,dx209,dy209)
        dx210bis=dx209
        dy210bis=dy209
        if dd2==205 and dlol==204 :
            monCanevas.move(balle209,-8000,-8000)
            dlol=205

        monCanevas.move(balle210,dx210,dy210)
        dx211bis=dx210
        dy211bis=dy210
        if dd2==206 and dlol==205 :
            monCanevas.move(balle210,-8000,-8000)
            dlol=206

        monCanevas.move(balle211,dx211,dy211)
        dx212bis=dx211
        dy212bis=dy211
        if dd2==207 and dlol==206 :
            monCanevas.move(balle211,-8000,-8000)
            dlol=207

        monCanevas.move(balle212,dx212,dy212)
        dx213bis=dx212
        dy213bis=dy212
        if dd2==208 and dlol==207 :
            monCanevas.move(balle212,-8000,-8000)
            dlol=208

        monCanevas.move(balle213,dx213,dy213)
        dx214bis=dx213
        dy214bis=dy213
        if dd2==209 and dlol==208 :
            monCanevas.move(balle213,-8000,-8000)
            dlol=209

        monCanevas.move(balle214,dx214,dy214)
        dx215bis=dx214
        dy215bis=dy214
        if dd2==210 and dlol==209 :
            monCanevas.move(balle214,-8000,-8000)
            dlol=210

        monCanevas.move(balle215,dx215,dy215)
        dx216bis=dx215
        dy216bis=dy215
        if dd2==211 and dlol==210 :
            monCanevas.move(balle215,-8000,-8000)
            dlol=211

        monCanevas.move(balle216,dx216,dy216)
        dx217bis=dx216
        dy217bis=dy216
        if dd2==212 and dlol==211 :
            monCanevas.move(balle216,-8000,-8000)
            dlol=212

        monCanevas.move(balle217,dx217,dy217)
        dx218bis=dx217
        dy218bis=dy217
        if dd2==213 and dlol==212 :
            monCanevas.move(balle217,-8000,-8000)
            dlol=213

        monCanevas.move(balle218,dx218,dy218)
        dx219bis=dx218
        dy219bis=dy218
        if dd2==214 and dlol==213 :
            monCanevas.move(balle218,-8000,-8000)
            dlol=214

        monCanevas.move(balle219,dx219,dy219)
        dx220bis=dx219
        dy220bis=dy219
        if dd2==215 and dlol==214 :
            monCanevas.move(balle219,-8000,-8000)
            dlol=215

        monCanevas.move(balle220,dx220,dy220)
        dx221bis=dx220
        dy221bis=dy220
        if dd2==216 and dlol==215 :
            monCanevas.move(balle220,-8000,-8000)
            dlol=216

        monCanevas.move(balle221,dx221,dy221)
        dx222bis=dx221
        dy222bis=dy221
        if dd2==217 and dlol==216 :
            monCanevas.move(balle221,-8000,-8000)
            dlol=217

        monCanevas.move(balle222,dx222,dy222)
        dx223bis=dx222
        dy223bis=dy222
        if dd2==218 and dlol==217 :
            monCanevas.move(balle222,-8000,-8000)
            dlol=218

        monCanevas.move(balle223,dx223,dy223)
        dx224bis=dx223
        dy224bis=dy223
        if dd2==219 and dlol==218 :
            monCanevas.move(balle223,-8000,-8000)
            dlol=219

        monCanevas.move(balle224,dx224,dy224)
        dx225bis=dx224
        dy225bis=dy224
        if dd2==220 and dlol==219 :
            monCanevas.move(balle224,-8000,-8000)
            dlol=220

        monCanevas.move(balle225,dx225,dy225)
        dx226bis=dx225
        dy226bis=dy225
        if dd2==221 and dlol==220 :
            monCanevas.move(balle225,-8000,-8000)
            dlol=221

        monCanevas.move(balle226,dx226,dy226)
        dx227bis=dx226
        dy227bis=dy226
        if dd2==222 and dlol==221 :
            monCanevas.move(balle226,-8000,-8000)
            dlol=222

        monCanevas.move(balle227,dx227,dy227)
        dx228bis=dx227
        dy228bis=dy227
        if dd2==223 and dlol==222 :
            monCanevas.move(balle227,-8000,-8000)
            dlol=223

        monCanevas.move(balle228,dx228,dy228)
        dx229bis=dx228
        dy229bis=dy228
        if dd2==224 and dlol==223 :
            monCanevas.move(balle228,-8000,-8000)
            dlol=224

        monCanevas.move(balle229,dx229,dy229)
        dx230bis=dx229
        dy230bis=dy229
        if dd2==225 and dlol==224 :
            monCanevas.move(balle229,-8000,-8000)
            dlol=225

        monCanevas.move(balle230,dx230,dy230)
        dx231bis=dx230
        dy231bis=dy230
        if dd2==226 and dlol==225 :
            monCanevas.move(balle230,-8000,-8000)
            dlol=226

        monCanevas.move(balle231,dx231,dy231)
        dx232bis=dx231
        dy232bis=dy231
        if dd2==227 and dlol==226 :
            monCanevas.move(balle231,-8000,-8000)
            dlol=227

        monCanevas.move(balle232,dx232,dy232)
        dx233bis=dx232
        dy233bis=dy232
        if dd2==228 and dlol==227 :
            monCanevas.move(balle232,-8000,-8000)
            dlol=228

        monCanevas.move(balle233,dx233,dy233)
        dx234bis=dx233
        dy234bis=dy233
        if dd2==229 and dlol==228 :
            monCanevas.move(balle233,-8000,-8000)
            dlol=229

        monCanevas.move(balle234,dx234,dy234)
        dx235bis=dx234
        dy235bis=dy234
        if dd2==230 and dlol==229 :
            monCanevas.move(balle234,-8000,-8000)
            dlol=230

        monCanevas.move(balle235,dx235,dy235)
        dx236bis=dx235
        dy236bis=dy235
        if dd2==231 and dlol==230 :
            monCanevas.move(balle235,-8000,-8000)
            dlol=231

        monCanevas.move(balle236,dx236,dy236)
        dx237bis=dx236
        dy237bis=dy236
        if dd2==232 and dlol==231 :
            monCanevas.move(balle236,-8000,-8000)
            dlol=232

        monCanevas.move(balle237,dx237,dy237)
        dx238bis=dx237
        dy238bis=dy237
        if dd2==233 and dlol==232 :
            monCanevas.move(balle237,-8000,-8000)
            dlol=233

        monCanevas.move(balle238,dx238,dy238)
        dx239bis=dx238
        dy239bis=dy238
        if dd2==234 and dlol==233 :
            monCanevas.move(balle238,-8000,-8000)
            dlol=234

        monCanevas.move(balle239,dx239,dy239)
        dx240bis=dx239
        dy240bis=dy239
        if dd2==235 and dlol==234 :
            monCanevas.move(balle239,-8000,-8000)
            dlol=235

        monCanevas.move(balle240,dx240,dy240)
        dx241bis=dx240
        dy241bis=dy240
        if dd2==236 and dlol==235 :
            monCanevas.move(balle240,-8000,-8000)
            dlol=236

        monCanevas.move(balle241,dx241,dy241)
        dx242bis=dx241
        dy242bis=dy241
        if dd2==237 and dlol==236 :
            monCanevas.move(balle241,-8000,-8000)
            dlol=237

        monCanevas.move(balle242,dx242,dy242)
        dx243bis=dx242
        dy243bis=dy242
        if dd2==238 and dlol==237 :
            monCanevas.move(balle242,-8000,-8000)
            dlol=238

        monCanevas.move(balle243,dx243,dy243)
        dx244bis=dx243
        dy244bis=dy243
        if dd2==239 and dlol==238 :
            monCanevas.move(balle243,-8000,-8000)
            dlol=239

        monCanevas.move(balle244,dx244,dy244)
        dx245bis=dx244
        dy245bis=dy244
        if dd2==240 and dlol==239 :
            monCanevas.move(balle244,-8000,-8000)
            dlol=240

        monCanevas.move(balle245,dx245,dy245)
        dx246bis=dx245
        dy246bis=dy245
        if dd2==241 and dlol==240 :
            monCanevas.move(balle245,-8000,-8000)
            dlol=241

        monCanevas.move(balle246,dx246,dy246)
        dx247bis=dx246
        dy247bis=dy246
        if dd2==242 and dlol==241 :
            monCanevas.move(balle246,-8000,-8000)
            dlol=242

        monCanevas.move(balle247,dx247,dy247)
        dx248bis=dx247
        dy248bis=dy247
        if dd2==243 and dlol==242 :
            monCanevas.move(balle247,-8000,-8000)
            dlol=243

        monCanevas.move(balle248,dx248,dy248)
        dx249bis=dx248
        dy249bis=dy248
        if dd2==244 and dlol==243 :
            monCanevas.move(balle248,-8000,-8000)
            dlol=244

        monCanevas.move(balle249,dx249,dy249)
        dx250bis=dx249
        dy250bis=dy249
        if dd2==245 and dlol==244 :
            monCanevas.move(balle249,-8000,-8000)
            dlol=245

        monCanevas.move(balle250,dx250,dy250)
        dx251bis=dx250
        dy251bis=dy250
        if dd2==246 and dlol==245 :
            monCanevas.move(balle250,-8000,-8000)
            dlol=246

        monCanevas.move(balle251,dx251,dy251)
        dx252bis=dx251
        dy252bis=dy251
        if dd2==247 and dlol==246 :
            monCanevas.move(balle251,-8000,-8000)
            dlol=247

        monCanevas.move(balle252,dx252,dy252)
        dx253bis=dx252
        dy253bis=dy252
        if dd2==248 and dlol==247 :
            monCanevas.move(balle252,-8000,-8000)
            dlol=248

        monCanevas.move(balle253,dx253,dy253)
        dx254bis=dx253
        dy254bis=dy253
        if dd2==249 and dlol==248 :
            monCanevas.move(balle253,-8000,-8000)
            dlol=249

        monCanevas.move(balle254,dx254,dy254)
        dx255bis=dx254
        dy255bis=dy254
        if dd2==250 and dlol==249 :
            monCanevas.move(balle254,-8000,-8000)
            dlol=250

        monCanevas.move(balle255,dx255,dy255)
        dx256bis=dx255
        dy256bis=dy255
        if dd2==251 and dlol==250 :
            monCanevas.move(balle255,-8000,-8000)
            dlol=251

        monCanevas.move(balle256,dx256,dy256)
        dx257bis=dx256
        dy257bis=dy256
        if dd2==252 and dlol==251 :
            monCanevas.move(balle256,-8000,-8000)
            dlol=252

        monCanevas.move(balle257,dx257,dy257)
        dx258bis=dx257
        dy258bis=dy257
        if dd2==253 and dlol==252 :
            monCanevas.move(balle257,-8000,-8000)
            dlol=253

        monCanevas.move(balle258,dx258,dy258)
        dx259bis=dx258
        dy259bis=dy258
        if dd2==254 and dlol==253 :
            monCanevas.move(balle258,-8000,-8000)
            dlol=254

        monCanevas.move(balle259,dx259,dy259)
        dx260bis=dx259
        dy260bis=dy259
        if dd2==255 and dlol==254 :
            monCanevas.move(balle259,-8000,-8000)
            dlol=255

        monCanevas.move(balle260,dx260,dy260)
        dx261bis=dx260
        dy261bis=dy260
        if dd2==256 and dlol==255 :
            monCanevas.move(balle260,-8000,-8000)
            dlol=256

        monCanevas.move(balle261,dx261,dy261)
        dx262bis=dx261
        dy262bis=dy261
        if dd2==257 and dlol==256 :
            monCanevas.move(balle261,-8000,-8000)
            dlol=257

        monCanevas.move(balle262,dx262,dy262)
        dx263bis=dx262
        dy263bis=dy262
        if dd2==258 and dlol==257 :
            monCanevas.move(balle262,-8000,-8000)
            dlol=258

        monCanevas.move(balle263,dx263,dy263)
        dx264bis=dx263
        dy264bis=dy263
        if dd2==259 and dlol==258 :
            monCanevas.move(balle263,-8000,-8000)
            dlol=259

        monCanevas.move(balle264,dx264,dy264)
        dx265bis=dx264
        dy265bis=dy264
        if dd2==260 and dlol==259 :
            monCanevas.move(balle264,-8000,-8000)
            dlol=260

        monCanevas.move(balle265,dx265,dy265)
        dx266bis=dx265
        dy266bis=dy265
        if dd2==261 and dlol==260 :
            monCanevas.move(balle265,-8000,-8000)
            dlol=261

        monCanevas.move(balle266,dx266,dy266)
        dx267bis=dx266
        dy267bis=dy266
        if dd2==262 and dlol==261 :
            monCanevas.move(balle266,-8000,-8000)
            dlol=262

        monCanevas.move(balle267,dx267,dy267)
        dx268bis=dx267
        dy268bis=dy267
        if dd2==263 and dlol==262 :
            monCanevas.move(balle267,-8000,-8000)
            dlol=263

        monCanevas.move(balle268,dx268,dy268)
        dx269bis=dx268
        dy269bis=dy268
        if dd2==264 and dlol==263 :
            monCanevas.move(balle268,-8000,-8000)
            dlol=264

        monCanevas.move(balle269,dx269,dy269)
        dx270bis=dx269
        dy270bis=dy269
        if dd2==265 and dlol==264 :
            monCanevas.move(balle269,-8000,-8000)
            dlol=265

        monCanevas.move(balle270,dx270,dy270)
        dx271bis=dx270
        dy271bis=dy270
        if dd2==266 and dlol==265 :
            monCanevas.move(balle270,-8000,-8000)
            dlol=266

        monCanevas.move(balle271,dx271,dy271)
        dx272bis=dx271
        dy272bis=dy271
        if dd2==267 and dlol==266 :
            monCanevas.move(balle271,-8000,-8000)
            dlol=267

        monCanevas.move(balle272,dx272,dy272)
        dx273bis=dx272
        dy273bis=dy272
        if dd2==268 and dlol==267 :
            monCanevas.move(balle272,-8000,-8000)
            dlol=268

        monCanevas.move(balle273,dx273,dy273)
        dx274bis=dx273
        dy274bis=dy273
        if dd2==269 and dlol==268 :
            monCanevas.move(balle273,-8000,-8000)
            dlol=269

        monCanevas.move(balle274,dx274,dy274)
        dx275bis=dx274
        dy275bis=dy274
        if dd2==270 and dlol==269 :
            monCanevas.move(balle274,-8000,-8000)
            dlol=270

        monCanevas.move(balle275,dx275,dy275)
        dx276bis=dx275
        dy276bis=dy275
        if dd2==271 and dlol==270 :
            monCanevas.move(balle275,-8000,-8000)
            dlol=271

        monCanevas.move(balle276,dx276,dy276)
        dx277bis=dx276
        dy277bis=dy276
        if dd2==272 and dlol==271 :
            monCanevas.move(balle276,-8000,-8000)
            dlol=272

        monCanevas.move(balle277,dx277,dy277)
        dx278bis=dx277
        dy278bis=dy277
        if dd2==273 and dlol==272 :
            monCanevas.move(balle277,-8000,-8000)
            dlol=273

        monCanevas.move(balle278,dx278,dy278)
        dx279bis=dx278
        dy279bis=dy278
        if dd2==274 and dlol==273 :
            monCanevas.move(balle278,-8000,-8000)
            dlol=274

        monCanevas.move(balle279,dx279,dy279)
        dx280bis=dx279
        dy280bis=dy279
        if dd2==275 and dlol==274 :
            monCanevas.move(balle279,-8000,-8000)
            dlol=275

        monCanevas.move(balle280,dx280,dy280)
        dx281bis=dx280
        dy281bis=dy280
        if dd2==276 and dlol==275 :
            monCanevas.move(balle280,-8000,-8000)
            dlol=276

        monCanevas.move(balle281,dx281,dy281)
        dx282bis=dx281
        dy282bis=dy281
        if dd2==277 and dlol==276 :
            monCanevas.move(balle281,-8000,-8000)
            dlol=277

        monCanevas.move(balle282,dx282,dy282)
        dx283bis=dx282
        dy283bis=dy282
        if dd2==278 and dlol==277 :
            monCanevas.move(balle282,-8000,-8000)
            dlol=278

        monCanevas.move(balle283,dx283,dy283)
        dx284bis=dx283
        dy284bis=dy283
        if dd2==279 and dlol==278 :
            monCanevas.move(balle283,-8000,-8000)
            dlol=279

        monCanevas.move(balle284,dx284,dy284)
        dx285bis=dx284
        dy285bis=dy284
        if dd2==280 and dlol==279 :
            monCanevas.move(balle284,-8000,-8000)
            dlol=280

        monCanevas.move(balle285,dx285,dy285)
        dx286bis=dx285
        dy286bis=dy285
        if dd2==281 and dlol==280 :
            monCanevas.move(balle285,-8000,-8000)
            dlol=281

        monCanevas.move(balle286,dx286,dy286)
        dx287bis=dx286
        dy287bis=dy286
        if dd2==282 and dlol==281 :
            monCanevas.move(balle286,-8000,-8000)
            dlol=282

        monCanevas.move(balle287,dx287,dy287)
        dx288bis=dx287
        dy288bis=dy287
        if dd2==283 and dlol==282 :
            monCanevas.move(balle287,-8000,-8000)
            dlol=283

        monCanevas.move(balle288,dx288,dy288)
        dx289bis=dx288
        dy289bis=dy288
        if dd2==284 and dlol==283 :
            monCanevas.move(balle288,-8000,-8000)
            dlol=284

        monCanevas.move(balle289,dx289,dy289)
        dx290bis=dx289
        dy290bis=dy289
        if dd2==285 and dlol==284 :
            monCanevas.move(balle289,-8000,-8000)
            dlol=285

        monCanevas.move(balle290,dx290,dy290)
        dx291bis=dx290
        dy291bis=dy290
        if dd2==286 and dlol==285 :
            monCanevas.move(balle290,-8000,-8000)
            dlol=286

        monCanevas.move(balle291,dx291,dy291)
        dx292bis=dx291
        dy292bis=dy291
        if dd2==287 and dlol==286 :
            monCanevas.move(balle291,-8000,-8000)
            dlol=287

        monCanevas.move(balle292,dx292,dy292)
        dx293bis=dx292
        dy293bis=dy292
        if dd2==288 and dlol==287 :
            monCanevas.move(balle292,-8000,-8000)
            dlol=288

        monCanevas.move(balle293,dx293,dy293)
        dx294bis=dx293
        dy294bis=dy293
        if dd2==289 and dlol==288 :
            monCanevas.move(balle293,-8000,-8000)
            dlol=289

        monCanevas.move(balle294,dx294,dy294)
        dx295bis=dx294
        dy295bis=dy294
        if dd2==290 and dlol==289 :
            monCanevas.move(balle294,-8000,-8000)
            dlol=290

        monCanevas.move(balle295,dx295,dy295)
        dx296bis=dx295
        dy296bis=dy295
        if dd2==291 and dlol==290 :
            monCanevas.move(balle295,-8000,-8000)
            dlol=291

        monCanevas.move(balle296,dx296,dy296)
        dx297bis=dx296
        dy297bis=dy296
        if dd2==292 and dlol==291 :
            monCanevas.move(balle296,-8000,-8000)
            dlol=292

        monCanevas.move(balle297,dx297,dy297)
        dx298bis=dx297
        dy298bis=dy297
        if dd2==293 and dlol==292 :
            monCanevas.move(balle297,-8000,-8000)
            dlol=293

        monCanevas.move(balle298,dx298,dy298)
        dx299bis=dx298
        dy299bis=dy298
        if dd2==294 and dlol==293 :
            monCanevas.move(balle298,-8000,-8000)
            dlol=294

        monCanevas.move(balle299,dx299,dy299)
        dx300bis=dx299
        dy300bis=dy299
        if dd2==295 and dlol==294 :
            monCanevas.move(balle299,-8000,-8000)
            dlol=295

        monCanevas.move(balle300,dx300,dy300)
        dx301bis=dx300
        dy301bis=dy300
        if dd2==296 and dlol==295 :
            monCanevas.move(balle300,-8000,-8000)
            dlol=296

        monCanevas.move(balle301,dx301,dy301)
        dx302bis=dx301
        dy302bis=dy301
        if dd2==297 and dlol==296 :
            monCanevas.move(balle301,-8000,-8000)
            dlol=297

        monCanevas.move(balle302,dx302,dy302)
        dx303bis=dx302
        dy303bis=dy302
        if dd2==298 and dlol==297 :
            monCanevas.move(balle302,-8000,-8000)
            dlol=298

        monCanevas.move(balle303,dx303,dy303)
        dx304bis=dx303
        dy304bis=dy303
        if dd2==299 and dlol==298 :
            monCanevas.move(balle303,-8000,-8000)
            dlol=299

        monCanevas.move(balle304,dx304,dy304)
        dx305bis=dx304
        dy305bis=dy304
        if dd2==300 and dlol==299 :
            monCanevas.move(balle304,-8000,-8000)
            dlol=300

        monCanevas.move(balle305,dx305,dy305)
        dx306bis=dx305
        dy306bis=dy305
        if dd2==301 and dlol==300 :
            monCanevas.move(balle305,-8000,-8000)
            dlol=301

        monCanevas.move(balle306,dx306,dy306)
        dx307bis=dx306
        dy307bis=dy306
        if dd2==302 and dlol==301 :
            monCanevas.move(balle306,-8000,-8000)
            dlol=302

        monCanevas.move(balle307,dx307,dy307)
        dx308bis=dx307
        dy308bis=dy307
        if dd2==303 and dlol==302 :
            monCanevas.move(balle307,-8000,-8000)
            dlol=303

        monCanevas.move(balle308,dx308,dy308)
        dx309bis=dx308
        dy309bis=dy308
        if dd2==304 and dlol==303 :
            monCanevas.move(balle308,-8000,-8000)
            dlol=304

        monCanevas.move(balle309,dx309,dy309)
        dx310bis=dx309
        dy310bis=dy309
        if dd2==305 and dlol==304 :
            monCanevas.move(balle309,-8000,-8000)
            dlol=305

        monCanevas.move(balle310,dx310,dy310)
        dx311bis=dx310
        dy311bis=dy310
        if dd2==306 and dlol==305 :
            monCanevas.move(balle310,-8000,-8000)
            dlol=306

        monCanevas.move(balle311,dx311,dy311)
        dx312bis=dx311
        dy312bis=dy311
        if dd2==307 and dlol==306 :
            monCanevas.move(balle311,-8000,-8000)
            dlol=307

        monCanevas.move(balle312,dx312,dy312)
        dx313bis=dx312
        dy313bis=dy312
        if dd2==308 and dlol==307 :
            monCanevas.move(balle312,-8000,-8000)
            dlol=308

        monCanevas.move(balle313,dx313,dy313)
        dx314bis=dx313
        dy314bis=dy313
        if dd2==309 and dlol==308 :
            monCanevas.move(balle313,-8000,-8000)
            dlol=309

        monCanevas.move(balle314,dx314,dy314)
        dx315bis=dx314
        dy315bis=dy314
        if dd2==310 and dlol==309 :
            monCanevas.move(balle314,-8000,-8000)
            dlol=310

        monCanevas.move(balle315,dx315,dy315)
        dx316bis=dx315
        dy316bis=dy315
        if dd2==311 and dlol==310 :
            monCanevas.move(balle315,-8000,-8000)
            dlol=311

        monCanevas.move(balle316,dx316,dy316)
        dx317bis=dx316
        dy317bis=dy316
        if dd2==312 and dlol==311 :
            monCanevas.move(balle316,-8000,-8000)
            dlol=312

        monCanevas.move(balle317,dx317,dy317)
        dx318bis=dx317
        dy318bis=dy317
        if dd2==313 and dlol==312 :
            monCanevas.move(balle317,-8000,-8000)
            dlol=313

        monCanevas.move(balle318,dx318,dy318)
        dx319bis=dx318
        dy319bis=dy318
        if dd2==314 and dlol==313 :
            monCanevas.move(balle318,-8000,-8000)
            dlol=314

        monCanevas.move(balle319,dx319,dy319)
        dx320bis=dx319
        dy320bis=dy319
        if dd2==315 and dlol==314 :
            monCanevas.move(balle319,-8000,-8000)
            dlol=315

        monCanevas.move(balle320,dx320,dy320)
        dx321bis=dx320
        dy321bis=dy320
        if dd2==316 and dlol==315 :
            monCanevas.move(balle320,-8000,-8000)
            dlol=316

        monCanevas.move(balle321,dx321,dy321)
        dx322bis=dx321
        dy322bis=dy321
        if dd2==317 and dlol==316 :
            monCanevas.move(balle321,-8000,-8000)
            dlol=317

        monCanevas.move(balle322,dx322,dy322)
        dx323bis=dx322
        dy323bis=dy322
        if dd2==318 and dlol==317 :
            monCanevas.move(balle322,-8000,-8000)
            dlol=318

        monCanevas.move(balle323,dx323,dy323)
        dx324bis=dx323
        dy324bis=dy323
        if dd2==319 and dlol==318 :
            monCanevas.move(balle323,-8000,-8000)
            dlol=319

        monCanevas.move(balle324,dx324,dy324)
        dx325bis=dx324
        dy325bis=dy324
        if dd2==320 and dlol==319 :
            monCanevas.move(balle324,-8000,-8000)
            dlol=320

        monCanevas.move(balle325,dx325,dy325)
        dx326bis=dx325
        dy326bis=dy325
        if dd2==321 and dlol==320 :
            monCanevas.move(balle325,-8000,-8000)
            dlol=321

        monCanevas.move(balle326,dx326,dy326)
        dx327bis=dx326
        dy327bis=dy326
        if dd2==322 and dlol==321 :
            monCanevas.move(balle326,-8000,-8000)
            dlol=322

        monCanevas.move(balle327,dx327,dy327)
        dx328bis=dx327
        dy328bis=dy327
        if dd2==323 and dlol==322 :
            monCanevas.move(balle327,-8000,-8000)
            dlol=323

        monCanevas.move(balle328,dx328,dy328)
        dx329bis=dx328
        dy329bis=dy328
        if dd2==324 and dlol==323 :
            monCanevas.move(balle328,-8000,-8000)
            dlol=324

        monCanevas.move(balle329,dx329,dy329)
        dx330bis=dx329
        dy330bis=dy329
        if dd2==325 and dlol==324 :
            monCanevas.move(balle329,-8000,-8000)
            dlol=325

        monCanevas.move(balle330,dx330,dy330)
        dx331bis=dx330
        dy331bis=dy330
        if dd2==326 and dlol==325 :
            monCanevas.move(balle330,-8000,-8000)
            dlol=326

        monCanevas.move(balle331,dx331,dy331)
        dx332bis=dx331
        dy332bis=dy331
        if dd2==327 and dlol==326 :
            monCanevas.move(balle331,-8000,-8000)
            dlol=327

        monCanevas.move(balle332,dx332,dy332)
        dx333bis=dx332
        dy333bis=dy332
        if dd2==328 and dlol==327 :
            monCanevas.move(balle332,-8000,-8000)
            dlol=328

        monCanevas.move(balle333,dx333,dy333)
        dx334bis=dx333
        dy334bis=dy333
        if dd2==329 and dlol==328 :
            monCanevas.move(balle333,-8000,-8000)
            dlol=329

        monCanevas.move(balle334,dx334,dy334)
        dx335bis=dx334
        dy335bis=dy334
        if dd2==330 and dlol==329 :
            monCanevas.move(balle334,-8000,-8000)
            dlol=330

        monCanevas.move(balle335,dx335,dy335)
        dx336bis=dx335
        dy336bis=dy335
        if dd2==331 and dlol==330 :
            monCanevas.move(balle335,-8000,-8000)
            dlol=331

        monCanevas.move(balle336,dx336,dy336)
        dx337bis=dx336
        dy337bis=dy336
        if dd2==332 and dlol==331 :
            monCanevas.move(balle336,-8000,-8000)
            dlol=332

        monCanevas.move(balle337,dx337,dy337)
        dx338bis=dx337
        dy338bis=dy337
        if dd2==333 and dlol==332 :
            monCanevas.move(balle337,-8000,-8000)
            dlol=333

        monCanevas.move(balle338,dx338,dy338)
        dx339bis=dx338
        dy339bis=dy338
        if dd2==334 and dlol==333 :
            monCanevas.move(balle338,-8000,-8000)
            dlol=334

        monCanevas.move(balle339,dx339,dy339)
        dx340bis=dx339
        dy340bis=dy339
        if dd2==335 and dlol==334 :
            monCanevas.move(balle339,-8000,-8000)
            dlol=335

        monCanevas.move(balle340,dx340,dy340)
        dx341bis=dx340
        dy341bis=dy340
        if dd2==336 and dlol==335 :
            monCanevas.move(balle340,-8000,-8000)
            dlol=336

        monCanevas.move(balle341,dx341,dy341)
        dx342bis=dx341
        dy342bis=dy341
        if dd2==337 and dlol==336 :
            monCanevas.move(balle341,-8000,-8000)
            dlol=337

        monCanevas.move(balle342,dx342,dy342)
        dx343bis=dx342
        dy343bis=dy342
        if dd2==338 and dlol==337 :
            monCanevas.move(balle342,-8000,-8000)
            dlol=338

        monCanevas.move(balle343,dx343,dy343)
        dx344bis=dx343
        dy344bis=dy343
        if dd2==339 and dlol==338 :
            monCanevas.move(balle343,-8000,-8000)
            dlol=339

        monCanevas.move(balle344,dx344,dy344)
        dx345bis=dx344
        dy345bis=dy344
        if dd2==340 and dlol==339 :
            monCanevas.move(balle344,-8000,-8000)
            dlol=340

        monCanevas.move(balle345,dx345,dy345)
        dx346bis=dx345
        dy346bis=dy345
        if dd2==341 and dlol==340 :
            monCanevas.move(balle345,-8000,-8000)
            dlol=341

        monCanevas.move(balle346,dx346,dy346)
        dx347bis=dx346
        dy347bis=dy346
        if dd2==342 and dlol==341 :
            monCanevas.move(balle346,-8000,-8000)
            dlol=342

        monCanevas.move(balle347,dx347,dy347)
        dx348bis=dx347
        dy348bis=dy347
        if dd2==343 and dlol==342 :
            monCanevas.move(balle347,-8000,-8000)
            dlol=343

        monCanevas.move(balle348,dx348,dy348)
        dx349bis=dx348
        dy349bis=dy348
        if dd2==344 and dlol==343 :
            monCanevas.move(balle348,-8000,-8000)
            dlol=344

        monCanevas.move(balle349,dx349,dy349)
        dx350bis=dx349
        dy350bis=dy349
        if dd2==345 and dlol==344 :
            monCanevas.move(balle349,-8000,-8000)
            dlol=345

        monCanevas.move(balle350,dx350,dy350)
        dx351bis=dx350
        dy351bis=dy350
        if dd2==346 and dlol==345 :
            monCanevas.move(balle350,-8000,-8000)
            dlol=346

        monCanevas.move(balle351,dx351,dy351)
        dx352bis=dx351
        dy352bis=dy351
        if dd2==347 and dlol==346 :
            monCanevas.move(balle351,-8000,-8000)
            dlol=347

        monCanevas.move(balle352,dx352,dy352)
        dx353bis=dx352
        dy353bis=dy352
        if dd2==348 and dlol==347 :
            monCanevas.move(balle352,-8000,-8000)
            dlol=348

        monCanevas.move(balle353,dx353,dy353)
        dx354bis=dx353
        dy354bis=dy353
        if dd2==349 and dlol==348 :
            monCanevas.move(balle353,-8000,-8000)
            dlol=349

        monCanevas.move(balle354,dx354,dy354)
        dx355bis=dx354
        dy355bis=dy354
        if dd2==350 and dlol==349 :
            monCanevas.move(balle354,-8000,-8000)
            dlol=350

        monCanevas.move(balle355,dx355,dy355)
        dx356bis=dx355
        dy356bis=dy355
        if dd2==351 and dlol==350 :
            monCanevas.move(balle355,-8000,-8000)
            dlol=351

        monCanevas.move(balle356,dx356,dy356)
        dx357bis=dx356
        dy357bis=dy356
        if dd2==352 and dlol==351 :
            monCanevas.move(balle356,-8000,-8000)
            dlol=352

        monCanevas.move(balle357,dx357,dy357)
        dx358bis=dx357
        dy358bis=dy357
        if dd2==353 and dlol==352 :
            monCanevas.move(balle357,-8000,-8000)
            dlol=353

        monCanevas.move(balle358,dx358,dy358)
        dx359bis=dx358
        dy359bis=dy358
        if dd2==354 and dlol==353 :
            monCanevas.move(balle358,-8000,-8000)
            dlol=354

        monCanevas.move(balle359,dx359,dy359)
        dx360bis=dx359
        dy360bis=dy359
        if dd2==355 and dlol==354 :
            monCanevas.move(balle359,-8000,-8000)
            dlol=355

        monCanevas.move(balle360,dx360,dy360)
        dx361bis=dx360
        dy361bis=dy360
        if dd2==356 and dlol==355 :
            monCanevas.move(balle360,-8000,-8000)
            dlol=356

        monCanevas.move(balle361,dx361,dy361)
        dx362bis=dx361
        dy362bis=dy361
        if dd2==357 and dlol==356 :
            monCanevas.move(balle361,-8000,-8000)
            dlol=357

        monCanevas.move(balle362,dx362,dy362)
        dx363bis=dx362
        dy363bis=dy362
        if dd2==358 and dlol==357 :
            monCanevas.move(balle362,-8000,-8000)
            dlol=358

        monCanevas.move(balle363,dx363,dy363)
        dx364bis=dx363
        dy364bis=dy363
        if dd2==359 and dlol==358 :
            monCanevas.move(balle363,-8000,-8000)
            dlol=359

        monCanevas.move(balle364,dx364,dy364)
        dx365bis=dx364
        dy365bis=dy364
        if dd2==360 and dlol==359 :
            monCanevas.move(balle364,-8000,-8000)
            dlol=360

        monCanevas.move(balle365,dx365,dy365)
        dx366bis=dx365
        dy366bis=dy365
        if dd2==361 and dlol==360 :
            monCanevas.move(balle365,-8000,-8000)
            dlol=361

        monCanevas.move(balle366,dx366,dy366)
        dx367bis=dx366
        dy367bis=dy366
        if dd2==362 and dlol==361 :
            monCanevas.move(balle366,-8000,-8000)
            dlol=362

        monCanevas.move(balle367,dx367,dy367)
        dx368bis=dx367
        dy368bis=dy367
        if dd2==363 and dlol==362 :
            monCanevas.move(balle367,-8000,-8000)
            dlol=363

        monCanevas.move(balle368,dx368,dy368)
        dx369bis=dx368
        dy369bis=dy368
        if dd2==364 and dlol==363 :
            monCanevas.move(balle368,-8000,-8000)
            dlol=364

        monCanevas.move(balle369,dx369,dy369)
        dx370bis=dx369
        dy370bis=dy369
        if dd2==365 and dlol==364 :
            monCanevas.move(balle369,-8000,-8000)
            dlol=365

        monCanevas.move(balle370,dx370,dy370)
        dx371bis=dx370
        dy371bis=dy370
        if dd2==366 and dlol==365 :
            monCanevas.move(balle370,-8000,-8000)
            dlol=366

        monCanevas.move(balle371,dx371,dy371)
        dx372bis=dx371
        dy372bis=dy371
        if dd2==367 and dlol==366 :
            monCanevas.move(balle371,-8000,-8000)
            dlol=367

        monCanevas.move(balle372,dx372,dy372)
        dx373bis=dx372
        dy373bis=dy372
        if dd2==368 and dlol==367 :
            monCanevas.move(balle372,-8000,-8000)
            dlol=368

        monCanevas.move(balle373,dx373,dy373)
        dx374bis=dx373
        dy374bis=dy373
        if dd2==369 and dlol==368 :
            monCanevas.move(balle373,-8000,-8000)
            dlol=369

        monCanevas.move(balle374,dx374,dy374)
        dx375bis=dx374
        dy375bis=dy374
        if dd2==370 and dlol==369 :
            monCanevas.move(balle374,-8000,-8000)
            dlol=370

        monCanevas.move(balle375,dx375,dy375)
        dx376bis=dx375
        dy376bis=dy375
        if dd2==371 and dlol==370 :
            monCanevas.move(balle375,-8000,-8000)
            dlol=371

        monCanevas.move(balle376,dx376,dy376)
        dx377bis=dx376
        dy377bis=dy376
        if dd2==372 and dlol==371 :
            monCanevas.move(balle376,-8000,-8000)
            dlol=372

        monCanevas.move(balle377,dx377,dy377)
        dx378bis=dx377
        dy378bis=dy377
        if dd2==373 and dlol==372 :
            monCanevas.move(balle377,-8000,-8000)
            dlol=373

        monCanevas.move(balle378,dx378,dy378)
        dx379bis=dx378
        dy379bis=dy378
        if dd2==374 and dlol==373 :
            monCanevas.move(balle378,-8000,-8000)
            dlol=374

        monCanevas.move(balle379,dx379,dy379)
        dx380bis=dx379
        dy380bis=dy379
        if dd2==375 and dlol==374 :
            monCanevas.move(balle379,-8000,-8000)
            dlol=375

        monCanevas.move(balle380,dx380,dy380)
        dx381bis=dx380
        dy381bis=dy380
        if dd2==376 and dlol==375 :
            monCanevas.move(balle380,-8000,-8000)
            dlol=376

        monCanevas.move(balle381,dx381,dy381)
        dx382bis=dx381
        dy382bis=dy381
        if dd2==377 and dlol==376 :
            monCanevas.move(balle381,-8000,-8000)
            dlol=377

        monCanevas.move(balle382,dx382,dy382)
        dx383bis=dx382
        dy383bis=dy382
        if dd2==378 and dlol==377 :
            monCanevas.move(balle382,-8000,-8000)
            dlol=378

        monCanevas.move(balle383,dx383,dy383)
        dx384bis=dx383
        dy384bis=dy383
        if dd2==379 and dlol==378 :
            monCanevas.move(balle383,-8000,-8000)
            dlol=379

        monCanevas.move(balle384,dx384,dy384)
        dx385bis=dx384
        dy385bis=dy384
        if dd2==380 and dlol==379 :
            monCanevas.move(balle384,-8000,-8000)
            dlol=380

        monCanevas.move(balle385,dx385,dy385)
        dx386bis=dx385
        dy386bis=dy385
        if dd2==381 and dlol==380 :
            monCanevas.move(balle385,-8000,-8000)
            dlol=381

        monCanevas.move(balle386,dx386,dy386)
        dx387bis=dx386
        dy387bis=dy386
        if dd2==382 and dlol==381 :
            monCanevas.move(balle386,-8000,-8000)
            dlol=382

        monCanevas.move(balle387,dx387,dy387)
        dx388bis=dx387
        dy388bis=dy387
        if dd2==383 and dlol==382 :
            monCanevas.move(balle387,-8000,-8000)
            dlol=383

        monCanevas.move(balle388,dx388,dy388)
        dx389bis=dx388
        dy389bis=dy388
        if dd2==384 and dlol==383 :
            monCanevas.move(balle388,-8000,-8000)
            dlol=384

        monCanevas.move(balle389,dx389,dy389)
        dx390bis=dx389
        dy390bis=dy389
        if dd2==385 and dlol==384 :
            monCanevas.move(balle389,-8000,-8000)
            dlol=385

        monCanevas.move(balle390,dx390,dy390)
        dx391bis=dx390
        dy391bis=dy390
        if dd2==386 and dlol==385 :
            monCanevas.move(balle390,-8000,-8000)
            dlol=386

        monCanevas.move(balle391,dx391,dy391)
        dx392bis=dx391
        dy392bis=dy391
        if dd2==387 and dlol==386 :
            monCanevas.move(balle391,-8000,-8000)
            dlol=387

        monCanevas.move(balle392,dx392,dy392)
        dx393bis=dx392
        dy393bis=dy392
        if dd2==388 and dlol==387 :
            monCanevas.move(balle392,-8000,-8000)
            dlol=388

        monCanevas.move(balle393,dx393,dy393)
        dx394bis=dx393
        dy394bis=dy393
        if dd2==389 and dlol==388 :
            monCanevas.move(balle393,-8000,-8000)
            dlol=389

        monCanevas.move(balle394,dx394,dy394)
        dx395bis=dx394
        dy395bis=dy394
        if dd2==390 and dlol==389 :
            monCanevas.move(balle394,-8000,-8000)
            dlol=390

        monCanevas.move(balle395,dx395,dy395)
        dx396bis=dx395
        dy396bis=dy395
        if dd2==391 and dlol==390 :
            monCanevas.move(balle395,-8000,-8000)
            dlol=391

        monCanevas.move(balle396,dx396,dy396)
        dx397bis=dx396
        dy397bis=dy396
        if dd2==392 and dlol==391 :
            monCanevas.move(balle396,-8000,-8000)
            dlol=392

        monCanevas.move(balle397,dx397,dy397)
        dx398bis=dx397
        dy398bis=dy397
        if dd2==393 and dlol==392 :
            monCanevas.move(balle397,-8000,-8000)
            dlol=393

        monCanevas.move(balle398,dx398,dy398)
        dx399bis=dx398
        dy399bis=dy398
        if dd2==394 and dlol==393 :
            monCanevas.move(balle398,-8000,-8000)
            dlol=394

        monCanevas.move(balle399,dx399,dy399)
        dx400bis=dx399
        dy400bis=dy399
        if dd2==395 and dlol==394 :
            monCanevas.move(balle399,-8000,-8000)
            dlol=395

        monCanevas.move(balle400,dx400,dy400)
        dx401bis=dx400
        dy401bis=dy400
        if dd2==396 and dlol==395 :
            monCanevas.move(balle400,-8000,-8000)
            dlol=396

        monCanevas.move(balle401,dx401,dy401)
        dx402bis=dx401
        dy402bis=dy401
        if dd2==397 and dlol==396 :
            monCanevas.move(balle401,-8000,-8000)
            dlol=397

        monCanevas.move(balle402,dx402,dy402)
        dx403bis=dx402
        dy403bis=dy402
        if dd2==398 and dlol==397 :
            monCanevas.move(balle402,-8000,-8000)
            dlol=398

        monCanevas.move(balle403,dx403,dy403)
        dx404bis=dx403
        dy404bis=dy403
        if dd2==399 and dlol==398 :
            monCanevas.move(balle403,-8000,-8000)
            dlol=399

        monCanevas.move(balle404,dx404,dy404)
        dx405bis=dx404
        dy405bis=dy404
        if dd2==400 and dlol==399 :
            monCanevas.move(balle404,-8000,-8000)
            dlol=400

        monCanevas.move(balle405,dx405,dy405)
        dx406bis=dx405
        dy406bis=dy405
        if dd2==401 and dlol==400 :
            monCanevas.move(balle405,-8000,-8000)
            dlol=401

        monCanevas.move(balle406,dx406,dy406)
        dx407bis=dx406
        dy407bis=dy406
        if dd2==402 and dlol==401 :
            monCanevas.move(balle406,-8000,-8000)
            dlol=402

        monCanevas.move(balle407,dx407,dy407)
        dx408bis=dx407
        dy408bis=dy407
        if dd2==403 and dlol==402 :
            monCanevas.move(balle407,-8000,-8000)
            dlol=403

        monCanevas.move(balle408,dx408,dy408)
        dx409bis=dx408
        dy409bis=dy408
        if dd2==404 and dlol==403 :
            monCanevas.move(balle408,-8000,-8000)
            dlol=404

        monCanevas.move(balle409,dx409,dy409)
        dx410bis=dx409
        dy410bis=dy409
        if dd2==405 and dlol==404 :
            monCanevas.move(balle409,-8000,-8000)
            dlol=405

        monCanevas.move(balle410,dx410,dy410)
        dx411bis=dx410
        dy411bis=dy410
        if dd2==406 and dlol==405 :
            monCanevas.move(balle410,-8000,-8000)
            dlol=406

        monCanevas.move(balle411,dx411,dy411)
        dx412bis=dx411
        dy412bis=dy411
        if dd2==407 and dlol==406 :
            monCanevas.move(balle411,-8000,-8000)
            dlol=407

        monCanevas.move(balle412,dx412,dy412)
        dx413bis=dx412
        dy413bis=dy412
        if dd2==408 and dlol==407 :
            monCanevas.move(balle412,-8000,-8000)
            dlol=408

        monCanevas.move(balle413,dx413,dy413)
        dx414bis=dx413
        dy414bis=dy413
        if dd2==409 and dlol==408 :
            monCanevas.move(balle413,-8000,-8000)
            dlol=409

        monCanevas.move(balle414,dx414,dy414)
        dx415bis=dx414
        dy415bis=dy414
        if dd2==410 and dlol==409 :
            monCanevas.move(balle414,-8000,-8000)
            dlol=410

        monCanevas.move(balle415,dx415,dy415)
        dx416bis=dx415
        dy416bis=dy415
        if dd2==411 and dlol==410 :
            monCanevas.move(balle415,-8000,-8000)
            dlol=411

        monCanevas.move(balle416,dx416,dy416)
        dx417bis=dx416
        dy417bis=dy416
        if dd2==412 and dlol==411 :
            monCanevas.move(balle416,-8000,-8000)
            dlol=412

        monCanevas.move(balle417,dx417,dy417)
        dx418bis=dx417
        dy418bis=dy417
        if dd2==413 and dlol==412 :
            monCanevas.move(balle417,-8000,-8000)
            dlol=413

        monCanevas.move(balle418,dx418,dy418)
        dx419bis=dx418
        dy419bis=dy418
        if dd2==414 and dlol==413 :
            monCanevas.move(balle418,-8000,-8000)
            dlol=414

        monCanevas.move(balle419,dx419,dy419)
        dx420bis=dx419
        dy420bis=dy419
        if dd2==415 and dlol==414 :
            monCanevas.move(balle419,-8000,-8000)
            dlol=415

        monCanevas.move(balle420,dx420,dy420)
        dx421bis=dx420
        dy421bis=dy420
        if dd2==416 and dlol==415 :
            monCanevas.move(balle420,-8000,-8000)
            dlol=416

        monCanevas.move(balle421,dx421,dy421)
        dx422bis=dx421
        dy422bis=dy421
        if dd2==417 and dlol==416 :
            monCanevas.move(balle421,-8000,-8000)
            dlol=417

        monCanevas.move(balle422,dx422,dy422)
        dx423bis=dx422
        dy423bis=dy422
        if dd2==418 and dlol==417 :
            monCanevas.move(balle422,-8000,-8000)
            dlol=418

        monCanevas.move(balle423,dx423,dy423)
        dx424bis=dx423
        dy424bis=dy423
        if dd2==419 and dlol==418 :
            monCanevas.move(balle423,-8000,-8000)
            dlol=419

        monCanevas.move(balle424,dx424,dy424)
        dx425bis=dx424
        dy425bis=dy424
        if dd2==420 and dlol==419 :
            monCanevas.move(balle424,-8000,-8000)
            dlol=420

        monCanevas.move(balle425,dx425,dy425)
        dx426bis=dx425
        dy426bis=dy425
        if dd2==421 and dlol==420 :
            monCanevas.move(balle425,-8000,-8000)
            dlol=421

        monCanevas.move(balle426,dx426,dy426)
        dx427bis=dx426
        dy427bis=dy426
        if dd2==422 and dlol==421 :
            monCanevas.move(balle426,-8000,-8000)
            dlol=422

        monCanevas.move(balle427,dx427,dy427)
        dx428bis=dx427
        dy428bis=dy427
        if dd2==423 and dlol==422 :
            monCanevas.move(balle427,-8000,-8000)
            dlol=423

        monCanevas.move(balle428,dx428,dy428)
        dx429bis=dx428
        dy429bis=dy428
        if dd2==424 and dlol==423 :
            monCanevas.move(balle428,-8000,-8000)
            dlol=424

        monCanevas.move(balle429,dx429,dy429)
        dx430bis=dx429
        dy430bis=dy429
        if dd2==425 and dlol==424 :
            monCanevas.move(balle429,-8000,-8000)
            dlol=425

        monCanevas.move(balle430,dx430,dy430)
        dx431bis=dx430
        dy431bis=dy430
        if dd2==426 and dlol==425 :
            monCanevas.move(balle430,-8000,-8000)
            dlol=426

        monCanevas.move(balle431,dx431,dy431)
        dx432bis=dx431
        dy432bis=dy431
        if dd2==427 and dlol==426 :
            monCanevas.move(balle431,-8000,-8000)
            dlol=427

        monCanevas.move(balle432,dx432,dy432)
        dx433bis=dx432
        dy433bis=dy432
        if dd2==428 and dlol==427 :
            monCanevas.move(balle432,-8000,-8000)
            dlol=428

        monCanevas.move(balle433,dx433,dy433)
        dx434bis=dx433
        dy434bis=dy433
        if dd2==429 and dlol==428 :
            monCanevas.move(balle433,-8000,-8000)
            dlol=429

        monCanevas.move(balle434,dx434,dy434)
        dx435bis=dx434
        dy435bis=dy434
        if dd2==430 and dlol==429 :
            monCanevas.move(balle434,-8000,-8000)
            dlol=430

        monCanevas.move(balle435,dx435,dy435)
        dx436bis=dx435
        dy436bis=dy435
        if dd2==431 and dlol==430 :
            monCanevas.move(balle435,-8000,-8000)
            dlol=431

        monCanevas.move(balle436,dx436,dy436)
        dx437bis=dx436
        dy437bis=dy436
        if dd2==432 and dlol==431 :
            monCanevas.move(balle436,-8000,-8000)
            dlol=432

        monCanevas.move(balle437,dx437,dy437)
        dx438bis=dx437
        dy438bis=dy437
        if dd2==433 and dlol==432 :
            monCanevas.move(balle437,-8000,-8000)
            dlol=433

        monCanevas.move(balle438,dx438,dy438)
        dx439bis=dx438
        dy439bis=dy438
        if dd2==434 and dlol==433 :
            monCanevas.move(balle438,-8000,-8000)
            dlol=434

        monCanevas.move(balle439,dx439,dy439)
        dx440bis=dx439
        dy440bis=dy439
        if dd2==435 and dlol==434 :
            monCanevas.move(balle439,-8000,-8000)
            dlol=435

        monCanevas.move(balle440,dx440,dy440)
        dx441bis=dx440
        dy441bis=dy440
        if dd2==436 and dlol==435 :
            monCanevas.move(balle440,-8000,-8000)
            dlol=436

        monCanevas.move(balle441,dx441,dy441)
        dx442bis=dx441
        dy442bis=dy441
        if dd2==437 and dlol==436 :
            monCanevas.move(balle441,-8000,-8000)
            dlol=437

        monCanevas.move(balle442,dx442,dy442)
        dx443bis=dx442
        dy443bis=dy442
        if dd2==438 and dlol==437 :
            monCanevas.move(balle442,-8000,-8000)
            dlol=438

        monCanevas.move(balle443,dx443,dy443)
        dx444bis=dx443
        dy444bis=dy443
        if dd2==439 and dlol==438 :
            monCanevas.move(balle443,-8000,-8000)
            dlol=439

        monCanevas.move(balle444,dx444,dy444)
        dx445bis=dx444
        dy445bis=dy444
        if dd2==440 and dlol==439 :
            monCanevas.move(balle444,-8000,-8000)
            dlol=440

        monCanevas.move(balle445,dx445,dy445)
        dx446bis=dx445
        dy446bis=dy445
        if dd2==441 and dlol==440 :
            monCanevas.move(balle445,-8000,-8000)
            dlol=441

        monCanevas.move(balle446,dx446,dy446)
        dx447bis=dx446
        dy447bis=dy446
        if dd2==442 and dlol==441 :
            monCanevas.move(balle446,-8000,-8000)
            dlol=442

        monCanevas.move(balle447,dx447,dy447)
        dx448bis=dx447
        dy448bis=dy447
        if dd2==443 and dlol==442 :
            monCanevas.move(balle447,-8000,-8000)
            dlol=443

        monCanevas.move(balle448,dx448,dy448)
        dx449bis=dx448
        dy449bis=dy448
        if dd2==444 and dlol==443 :
            monCanevas.move(balle448,-8000,-8000)
            dlol=444

        monCanevas.move(balle449,dx449,dy449)
        dx450bis=dx449
        dy450bis=dy449
        if dd2==445 and dlol==444 :
            monCanevas.move(balle449,-8000,-8000)
            dlol=445

        monCanevas.move(balle450,dx450,dy450)
        dx451bis=dx450
        dy451bis=dy450
        if dd2==446 and dlol==445 :
            monCanevas.move(balle450,-8000,-8000)
            dlol=446

        monCanevas.move(balle451,dx451,dy451)
        dx452bis=dx451
        dy452bis=dy451
        if dd2==447 and dlol==446 :
            monCanevas.move(balle451,-8000,-8000)
            dlol=447

        monCanevas.move(balle452,dx452,dy452)
        dx453bis=dx452
        dy453bis=dy452
        if dd2==448 and dlol==447 :
            monCanevas.move(balle452,-8000,-8000)
            dlol=448

        monCanevas.move(balle453,dx453,dy453)
        dx454bis=dx453
        dy454bis=dy453
        if dd2==449 and dlol==448 :
            monCanevas.move(balle453,-8000,-8000)
            dlol=449

        monCanevas.move(balle454,dx454,dy454)
        dx455bis=dx454
        dy455bis=dy454
        if dd2==450 and dlol==449 :
            monCanevas.move(balle454,-8000,-8000)
            dlol=450

        monCanevas.move(balle455,dx455,dy455)
        dx456bis=dx455
        dy456bis=dy455
        if dd2==451 and dlol==450 :
            monCanevas.move(balle455,-8000,-8000)
            dlol=451

        monCanevas.move(balle456,dx456,dy456)
        dx457bis=dx456
        dy457bis=dy456
        if dd2==452 and dlol==451 :
            monCanevas.move(balle456,-8000,-8000)
            dlol=452

        monCanevas.move(balle457,dx457,dy457)
        dx458bis=dx457
        dy458bis=dy457
        if dd2==453 and dlol==452 :
            monCanevas.move(balle457,-8000,-8000)
            dlol=453

        monCanevas.move(balle458,dx458,dy458)
        dx459bis=dx458
        dy459bis=dy458
        if dd2==454 and dlol==453 :
            monCanevas.move(balle458,-8000,-8000)
            dlol=454

        monCanevas.move(balle459,dx459,dy459)
        dx460bis=dx459
        dy460bis=dy459
        if dd2==455 and dlol==454 :
            monCanevas.move(balle459,-8000,-8000)
            dlol=455

        monCanevas.move(balle460,dx460,dy460)
        dx461bis=dx460
        dy461bis=dy460
        if dd2==456 and dlol==455 :
            monCanevas.move(balle460,-8000,-8000)
            dlol=456

        monCanevas.move(balle461,dx461,dy461)
        dx462bis=dx461
        dy462bis=dy461
        if dd2==457 and dlol==456 :
            monCanevas.move(balle461,-8000,-8000)
            dlol=457

        monCanevas.move(balle462,dx462,dy462)
        dx463bis=dx462
        dy463bis=dy462
        if dd2==458 and dlol==457 :
            monCanevas.move(balle462,-8000,-8000)
            dlol=458

        monCanevas.move(balle463,dx463,dy463)
        dx464bis=dx463
        dy464bis=dy463
        if dd2==459 and dlol==458 :
            monCanevas.move(balle463,-8000,-8000)
            dlol=459

        monCanevas.move(balle464,dx464,dy464)
        dx465bis=dx464
        dy465bis=dy464
        if dd2==460 and dlol==459 :
            monCanevas.move(balle464,-8000,-8000)
            dlol=460

        monCanevas.move(balle465,dx465,dy465)
        dx466bis=dx465
        dy466bis=dy465
        if dd2==461 and dlol==460 :
            monCanevas.move(balle465,-8000,-8000)
            dlol=461

        monCanevas.move(balle466,dx466,dy466)
        dx467bis=dx466
        dy467bis=dy466
        if dd2==462 and dlol==461 :
            monCanevas.move(balle466,-8000,-8000)
            dlol=462

        monCanevas.move(balle467,dx467,dy467)
        dx468bis=dx467
        dy468bis=dy467
        if dd2==463 and dlol==462 :
            monCanevas.move(balle467,-8000,-8000)
            dlol=463

        monCanevas.move(balle468,dx468,dy468)
        dx469bis=dx468
        dy469bis=dy468
        if dd2==464 and dlol==463 :
            monCanevas.move(balle468,-8000,-8000)
            dlol=464

        monCanevas.move(balle469,dx469,dy469)
        dx470bis=dx469
        dy470bis=dy469
        if dd2==465 and dlol==464 :
            monCanevas.move(balle469,-8000,-8000)
            dlol=465

        monCanevas.move(balle470,dx470,dy470)
        dx471bis=dx470
        dy471bis=dy470
        if dd2==466 and dlol==465 :
            monCanevas.move(balle470,-8000,-8000)
            dlol=466

        monCanevas.move(balle471,dx471,dy471)
        dx472bis=dx471
        dy472bis=dy471
        if dd2==467 and dlol==466 :
            monCanevas.move(balle471,-8000,-8000)
            dlol=467

        monCanevas.move(balle472,dx472,dy472)
        dx473bis=dx472
        dy473bis=dy472
        if dd2==468 and dlol==467 :
            monCanevas.move(balle472,-8000,-8000)
            dlol=468

        monCanevas.move(balle473,dx473,dy473)
        dx474bis=dx473
        dy474bis=dy473
        if dd2==469 and dlol==468 :
            monCanevas.move(balle473,-8000,-8000)
            dlol=469

        monCanevas.move(balle474,dx474,dy474)
        dx475bis=dx474
        dy475bis=dy474
        if dd2==470 and dlol==469 :
            monCanevas.move(balle474,-8000,-8000)
            dlol=470

        monCanevas.move(balle475,dx475,dy475)
        dx476bis=dx475
        dy476bis=dy475
        if dd2==471 and dlol==470 :
            monCanevas.move(balle475,-8000,-8000)
            dlol=471

        monCanevas.move(balle476,dx476,dy476)
        dx477bis=dx476
        dy477bis=dy476
        if dd2==472 and dlol==471 :
            monCanevas.move(balle476,-8000,-8000)
            dlol=472

        monCanevas.move(balle477,dx477,dy477)
        dx478bis=dx477
        dy478bis=dy477
        if dd2==473 and dlol==472 :
            monCanevas.move(balle477,-8000,-8000)
            dlol=473

        monCanevas.move(balle478,dx478,dy478)
        dx479bis=dx478
        dy479bis=dy478
        if dd2==474 and dlol==473 :
            monCanevas.move(balle478,-8000,-8000)
            dlol=474

        monCanevas.move(balle479,dx479,dy479)
        dx480bis=dx479
        dy480bis=dy479
        if dd2==475 and dlol==474 :
            monCanevas.move(balle479,-8000,-8000)
            dlol=475

        monCanevas.move(balle480,dx480,dy480)
        dx481bis=dx480
        dy481bis=dy480
        if dd2==476 and dlol==475 :
            monCanevas.move(balle480,-8000,-8000)
            dlol=476

        monCanevas.move(balle481,dx481,dy481)
        dx482bis=dx481
        dy482bis=dy481
        if dd2==477 and dlol==476 :
            monCanevas.move(balle481,-8000,-8000)
            dlol=477

        monCanevas.move(balle482,dx482,dy482)
        dx483bis=dx482
        dy483bis=dy482
        if dd2==478 and dlol==477 :
            monCanevas.move(balle482,-8000,-8000)
            dlol=478

        monCanevas.move(balle483,dx483,dy483)
        dx484bis=dx483
        dy484bis=dy483
        if dd2==479 and dlol==478 :
            monCanevas.move(balle483,-8000,-8000)
            dlol=479

        monCanevas.move(balle484,dx484,dy484)
        dx485bis=dx484
        dy485bis=dy484
        if dd2==480 and dlol==479 :
            monCanevas.move(balle484,-8000,-8000)
            dlol=480

        print(x2,a,y2,b)

        #definition de l'évenement le joueur mange une pomme
        if x-10<a<x+18 and y-10<b<y+18:
            croc()
            dd2=dd2+1
            c=coordoneex()
            d=coordoneey()
            a=c
            b=d
            #j'empeche la pomme d'apparaitre sur le snake (correctif)
            while x2-25<a<x2+25 and y2-25<b<y2+25 or x3-25<a<x3+25 and y3-25<b<y3+25 or x4-25<a<x4+25 and y4-25<b<y4+25 or x5-25<a<x5+25 and y5-25<b<y5+25 or x6-25<a<x6+25 and y6-25<b<y6+25 or x7-25<a<x7+25 and y7-25<b<y7+25 or x8-25<a<x8+25 and y8-25<b<y8+25 or x9-25<a<x9+25 and y9-25<b<y9+25 or x10-25<a<x10+25 and y10-25<b<y10+25 or x11-25<a<x11+25 and y11-25<b<y11+25 or x12-10<a<x12+18 and y12-10<b<y12+18 or x13-10<a<x13+18 and y13-10<b<y13+18 or x14-10<a<x14+18 and y14-10<b<y14+18 or x15-10<a<x15+18 and y15-10<b<y15+18 or x16-10<a<x16+18 and y16-10<b<y16+18 or x17-10<a<x17+18 and y17-10<b<y17+18 or x18-10<a<x18+18 and y18-10<b<y18+18 or x19-10<a<x19+18 and y19-10<b<y19+18 or x20-10<a<x20+18 and y20-10<b<y20+18 or x21-10<a<x21+18 and y21-10<b<y21+18 or x22-10<a<x22+18 and y22-10<b<y22+18 or x23-10<a<x23+18 and y23-10<b<y23+18 or x24-10<a<x24+18 and y24-10<b<y24+18 or x25-10<a<x25+18 and y25-10<b<y25+18:
                print("tomato")
                c=coordoneex()
                d=coordoneey()
                a=c
                b=d

            monCanevas.coords(Image1Canevas,c,d)

        #creation des colisions et du gamme over
        if isz>=4  :
            if x==x2 and y==y2 :
                dx=dx+8000
                dy=dy+8000
                Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                music=0
        if isz>=25 :
            if x==x3 and y==y3 or x==x4 and y==y4 or x==x5 and y==y5 or x==x6 and y==y6 or x==x7 and y==y7 or x==x8 and y==y8 or x==x9 and y==y9 or x==x10 and y==y10 or x==x11 and y==y11 or x==x12 and y==y12 or x==x13 and y==y13 or x==x14 and y==y14 or x==x15 and y==y15 or x==x16 and y==y16 or x==x17 and y==y17 or x==x18 and y==y18 or x==x19 and y==y19 or x==x20 and y==y20 or x==x21 and y==y21 or x==x22 and y==y22 or x==x23 and y==y23 or x==x24 and y==y24 or x==x25 and y==y25:
                dx=dx+8000
                dy=dy+8000
                Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                music=0

        if isz>=25 :
                if x==x25 and y==y25 or x==x25 and y==y25 :
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=26 :
                if x==x26 and y==y26 or x==x26 and y==y26:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=27 :
                if x==x27 and y==y27 or x==x27 and y==y27:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=28 :
                if x==x28 and y==y28 or x==x28 and y==y28:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=29 :
                if x==x29 and y==y29 or x==x29 and y==y29:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=30 :
                if x==x30 and y==y30 or x==x30 and y==y30:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=31 :
                if x==x31 and y==y31 or x==x31 and y==y31:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=32 :
                if x==x32 and y==y32 or x==x32 and y==y32:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=33 :
                if x==x33 and y==y33 or x==x33 and y==y33:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=34 :
                if x==x34 and y==y34 or x==x34 and y==y34:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=35 :
                if x==x35 and y==y35 or x==x35 and y==y35:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=36 :
                if x==x36 and y==y36 or x==x36 and y==y36:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=37 :
                if x==x37 and y==y37 or x==x37 and y==y37:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=38 :
                if x==x38 and y==y38 or x==x38 and y==y38:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=39 :
                if x==x39 and y==y39 or x==x39 and y==y39:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=40 :
                if x==x40 and y==y40 or x==x40 and y==y40:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=41 :
                if x==x41 and y==y41 or x==x41 and y==y41:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=42 :
                if x==x42 and y==y42 or x==x42 and y==y42:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=43 :
                if x==x43 and y==y43 or x==x43 and y==y43:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=44 :
                if x==x44 and y==y44 or x==x44 and y==y44:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=45 :
                if x==x45 and y==y45 or x==x45 and y==y45:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=46 :
                if x==x46 and y==y46 or x==x46 and y==y46:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=47 :
                if x==x47 and y==y47 or x==x47 and y==y47:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=48 :
                if x==x48 and y==y48 or x==x48 and y==y48:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=49 :
                if x==x49 and y==y49 or x==x49 and y==y49:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=50 :
                if x==x50 and y==y50 or x==x50 and y==y50:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=51 :
                if x==x51 and y==y51 or x==x51 and y==y51:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=52 :
                if x==x52 and y==y52 or x==x52 and y==y52:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=53 :
                if x==x53 and y==y53 or x==x53 and y==y53:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=54 :
                if x==x54 and y==y54 or x==x54 and y==y54:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=55 :
                if x==x55 and y==y55 or x==x55 and y==y55:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=56 :
                if x==x56 and y==y56 or x==x56 and y==y56:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=57 :
                if x==x57 and y==y57 or x==x57 and y==y57:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=58 :
                if x==x58 and y==y58 or x==x58 and y==y58:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=59 :
                if x==x59 and y==y59 or x==x59 and y==y59:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=60 :
                if x==x60 and y==y60 or x==x60 and y==y60:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=61 :
                if x==x61 and y==y61 or x==x61 and y==y61:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=62 :
                if x==x62 and y==y62 or x==x62 and y==y62:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=63 :
                if x==x63 and y==y63 or x==x63 and y==y63:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=64 :
                if x==x64 and y==y64 or x==x64 and y==y64:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=65 :
                if x==x65 and y==y65 or x==x65 and y==y65:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=66 :
                if x==x66 and y==y66 or x==x66 and y==y66:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=67 :
                if x==x67 and y==y67 or x==x67 and y==y67:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=68 :
                if x==x68 and y==y68 or x==x68 and y==y68:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=69 :
                if x==x69 and y==y69 or x==x69 and y==y69:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=70 :
                if x==x70 and y==y70 or x==x70 and y==y70:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=71 :
                if x==x71 and y==y71 or x==x71 and y==y71:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=72 :
                if x==x72 and y==y72 or x==x72 and y==y72:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=73 :
                if x==x73 and y==y73 or x==x73 and y==y73:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=74 :
                if x==x74 and y==y74 or x==x74 and y==y74:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=75 :
                if x==x75 and y==y75 or x==x75 and y==y75:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=76 :
                if x==x76 and y==y76 or x==x76 and y==y76:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=77 :
                if x==x77 and y==y77 or x==x77 and y==y77:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=78 :
                if x==x78 and y==y78 or x==x78 and y==y78:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=79 :
                if x==x79 and y==y79 or x==x79 and y==y79:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=80 :
                if x==x80 and y==y80 or x==x80 and y==y80:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=81 :
                if x==x81 and y==y81 or x==x81 and y==y81:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=82 :
                if x==x82 and y==y82 or x==x82 and y==y82:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=83 :
                if x==x83 and y==y83 or x==x83 and y==y83:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=84 :
                if x==x84 and y==y84 or x==x84 and y==y84:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=85 :
                if x==x85 and y==y85 or x==x85 and y==y85:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=86 :
                if x==x86 and y==y86 or x==x86 and y==y86:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=87 :
                if x==x87 and y==y87 or x==x87 and y==y87:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=88 :
                if x==x88 and y==y88 or x==x88 and y==y88:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=89 :
                if x==x89 and y==y89 or x==x89 and y==y89:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=90 :
                if x==x90 and y==y90 or x==x90 and y==y90:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=91 :
                if x==x91 and y==y91 or x==x91 and y==y91:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=92 :
                if x==x92 and y==y92 or x==x92 and y==y92:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=93 :
                if x==x93 and y==y93 or x==x93 and y==y93:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=94 :
                if x==x94 and y==y94 or x==x94 and y==y94:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=95 :
                if x==x95 and y==y95 or x==x95 and y==y95:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=96 :
                if x==x96 and y==y96 or x==x96 and y==y96:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=97 :
                if x==x97 and y==y97 or x==x97 and y==y97:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=98 :
                if x==x98 and y==y98 or x==x98 and y==y98:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=99 :
                if x==x99 and y==y99 or x==x99 and y==y99:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=100 :
                if x==x100 and y==y100 or x==x100 and y==y100:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=101 :
                if x==x101 and y==y101 or x==x101 and y==y101:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=102 :
                if x==x102 and y==y102 or x==x102 and y==y102:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=103 :
                if x==x103 and y==y103 or x==x103 and y==y103:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=104 :
                if x==x104 and y==y104 or x==x104 and y==y104:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=105 :
                if x==x105 and y==y105 or x==x105 and y==y105:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=106 :
                if x==x106 and y==y106 or x==x106 and y==y106:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=107 :
                if x==x107 and y==y107 or x==x107 and y==y107:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=108 :
                if x==x108 and y==y108 or x==x108 and y==y108:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=109 :
                if x==x109 and y==y109 or x==x109 and y==y109:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=110 :
                if x==x110 and y==y110 or x==x110 and y==y110:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=111 :
                if x==x111 and y==y111 or x==x111 and y==y111:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=112 :
                if x==x112 and y==y112 or x==x112 and y==y112:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=113 :
                if x==x113 and y==y113 or x==x113 and y==y113:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=114 :
                if x==x114 and y==y114 or x==x114 and y==y114:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=115 :
                if x==x115 and y==y115 or x==x115 and y==y115:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=116 :
                if x==x116 and y==y116 or x==x116 and y==y116:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=117 :
                if x==x117 and y==y117 or x==x117 and y==y117:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=118 :
                if x==x118 and y==y118 or x==x118 and y==y118:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=119 :
                if x==x119 and y==y119 or x==x119 and y==y119:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=120 :
                if x==x120 and y==y120 or x==x120 and y==y120:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=121 :
                if x==x121 and y==y121 or x==x121 and y==y121:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=122 :
                if x==x122 and y==y122 or x==x122 and y==y122:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=123 :
                if x==x123 and y==y123 or x==x123 and y==y123:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=124 :
                if x==x124 and y==y124 or x==x124 and y==y124:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=125 :
                if x==x125 and y==y125 or x==x125 and y==y125:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=126 :
                if x==x126 and y==y126 or x==x126 and y==y126:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=127 :
                if x==x127 and y==y127 or x==x127 and y==y127:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=128 :
                if x==x128 and y==y128 or x==x128 and y==y128:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=129 :
                if x==x129 and y==y129 or x==x129 and y==y129:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=130 :
                if x==x130 and y==y130 or x==x130 and y==y130:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=131 :
                if x==x131 and y==y131 or x==x131 and y==y131:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=132 :
                if x==x132 and y==y132 or x==x132 and y==y132:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=133 :
                if x==x133 and y==y133 or x==x133 and y==y133:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=134 :
                if x==x134 and y==y134 or x==x134 and y==y134:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=135 :
                if x==x135 and y==y135 or x==x135 and y==y135:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=136 :
                if x==x136 and y==y136 or x==x136 and y==y136:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=137 :
                if x==x137 and y==y137 or x==x137 and y==y137:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=138 :
                if x==x138 and y==y138 or x==x138 and y==y138:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=139 :
                if x==x139 and y==y139 or x==x139 and y==y139:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=140 :
                if x==x140 and y==y140 or x==x140 and y==y140:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=141 :
                if x==x141 and y==y141 or x==x141 and y==y141:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=142 :
                if x==x142 and y==y142 or x==x142 and y==y142:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=143 :
                if x==x143 and y==y143 or x==x143 and y==y143:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=144 :
                if x==x144 and y==y144 or x==x144 and y==y144:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=145 :
                if x==x145 and y==y145 or x==x145 and y==y145:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=146 :
                if x==x146 and y==y146 or x==x146 and y==y146:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=147 :
                if x==x147 and y==y147 or x==x147 and y==y147:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=148 :
                if x==x148 and y==y148 or x==x148 and y==y148:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=149 :
                if x==x149 and y==y149 or x==x149 and y==y149:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=150 :
                if x==x150 and y==y150 or x==x150 and y==y150:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=151 :
                if x==x151 and y==y151 or x==x151 and y==y151:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=152 :
                if x==x152 and y==y152 or x==x152 and y==y152:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=153 :
                if x==x153 and y==y153 or x==x153 and y==y153:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=154 :
                if x==x154 and y==y154 or x==x154 and y==y154:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=155 :
                if x==x155 and y==y155 or x==x155 and y==y155:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=156 :
                if x==x156 and y==y156 or x==x156 and y==y156:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=157 :
                if x==x157 and y==y157 or x==x157 and y==y157:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=158 :
                if x==x158 and y==y158 or x==x158 and y==y158:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=159 :
                if x==x159 and y==y159 or x==x159 and y==y159:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=160 :
                if x==x160 and y==y160 or x==x160 and y==y160:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=161 :
                if x==x161 and y==y161 or x==x161 and y==y161:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=162 :
                if x==x162 and y==y162 or x==x162 and y==y162:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=163 :
                if x==x163 and y==y163 or x==x163 and y==y163:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=164 :
                if x==x164 and y==y164 or x==x164 and y==y164:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=165 :
                if x==x165 and y==y165 or x==x165 and y==y165:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=166 :
                if x==x166 and y==y166 or x==x166 and y==y166:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=167 :
                if x==x167 and y==y167 or x==x167 and y==y167:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=168 :
                if x==x168 and y==y168 or x==x168 and y==y168:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=169 :
                if x==x169 and y==y169 or x==x169 and y==y169:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=170 :
                if x==x170 and y==y170 or x==x170 and y==y170:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=171 :
                if x==x171 and y==y171 or x==x171 and y==y171:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=172 :
                if x==x172 and y==y172 or x==x172 and y==y172:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=173 :
                if x==x173 and y==y173 or x==x173 and y==y173:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=174 :
                if x==x174 and y==y174 or x==x174 and y==y174:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=175 :
                if x==x175 and y==y175 or x==x175 and y==y175:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=176 :
                if x==x176 and y==y176 or x==x176 and y==y176:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=177 :
                if x==x177 and y==y177 or x==x177 and y==y177:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=178 :
                if x==x178 and y==y178 or x==x178 and y==y178:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=179 :
                if x==x179 and y==y179 or x==x179 and y==y179:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=180 :
                if x==x180 and y==y180 or x==x180 and y==y180:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=181 :
                if x==x181 and y==y181 or x==x181 and y==y181:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=182 :
                if x==x182 and y==y182 or x==x182 and y==y182:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=183 :
                if x==x183 and y==y183 or x==x183 and y==y183:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=184 :
                if x==x184 and y==y184 or x==x184 and y==y184:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=185 :
                if x==x185 and y==y185 or x==x185 and y==y185:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=186 :
                if x==x186 and y==y186 or x==x186 and y==y186:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=187 :
                if x==x187 and y==y187 or x==x187 and y==y187:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=188 :
                if x==x188 and y==y188 or x==x188 and y==y188:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=189 :
                if x==x189 and y==y189 or x==x189 and y==y189:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=190 :
                if x==x190 and y==y190 or x==x190 and y==y190:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=191 :
                if x==x191 and y==y191 or x==x191 and y==y191:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=192 :
                if x==x192 and y==y192 or x==x192 and y==y192:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=193 :
                if x==x193 and y==y193 or x==x193 and y==y193:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=194 :
                if x==x194 and y==y194 or x==x194 and y==y194:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=195 :
                if x==x195 and y==y195 or x==x195 and y==y195:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=196 :
                if x==x196 and y==y196 or x==x196 and y==y196:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=197 :
                if x==x197 and y==y197 or x==x197 and y==y197:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=198 :
                if x==x198 and y==y198 or x==x198 and y==y198:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=199 :
                if x==x199 and y==y199 or x==x199 and y==y199:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=200 :
                if x==x200 and y==y200 or x==x200 and y==y200:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=201 :
                if x==x201 and y==y201 or x==x201 and y==y201:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=202 :
                if x==x202 and y==y202 or x==x202 and y==y202:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=203 :
                if x==x203 and y==y203 or x==x203 and y==y203:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=204 :
                if x==x204 and y==y204 or x==x204 and y==y204:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=205 :
                if x==x205 and y==y205 or x==x205 and y==y205:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=206 :
                if x==x206 and y==y206 or x==x206 and y==y206:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=207 :
                if x==x207 and y==y207 or x==x207 and y==y207:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=208 :
                if x==x208 and y==y208 or x==x208 and y==y208:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=209 :
                if x==x209 and y==y209 or x==x209 and y==y209:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=210 :
                if x==x210 and y==y210 or x==x210 and y==y210:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=211 :
                if x==x211 and y==y211 or x==x211 and y==y211:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=212 :
                if x==x212 and y==y212 or x==x212 and y==y212:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=213 :
                if x==x213 and y==y213 or x==x213 and y==y213:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=214 :
                if x==x214 and y==y214 or x==x214 and y==y214:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=215 :
                if x==x215 and y==y215 or x==x215 and y==y215:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=216 :
                if x==x216 and y==y216 or x==x216 and y==y216:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=217 :
                if x==x217 and y==y217 or x==x217 and y==y217:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=218 :
                if x==x218 and y==y218 or x==x218 and y==y218:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=219 :
                if x==x219 and y==y219 or x==x219 and y==y219:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=220 :
                if x==x220 and y==y220 or x==x220 and y==y220:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=221 :
                if x==x221 and y==y221 or x==x221 and y==y221:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=222 :
                if x==x222 and y==y222 or x==x222 and y==y222:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=223 :
                if x==x223 and y==y223 or x==x223 and y==y223:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=224 :
                if x==x224 and y==y224 or x==x224 and y==y224:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=225 :
                if x==x225 and y==y225 or x==x225 and y==y225:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=226 :
                if x==x226 and y==y226 or x==x226 and y==y226:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=227 :
                if x==x227 and y==y227 or x==x227 and y==y227:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=228 :
                if x==x228 and y==y228 or x==x228 and y==y228:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=229 :
                if x==x229 and y==y229 or x==x229 and y==y229:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=230 :
                if x==x230 and y==y230 or x==x230 and y==y230:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=231 :
                if x==x231 and y==y231 or x==x231 and y==y231:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=232 :
                if x==x232 and y==y232 or x==x232 and y==y232:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=233 :
                if x==x233 and y==y233 or x==x233 and y==y233:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=234 :
                if x==x234 and y==y234 or x==x234 and y==y234:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=235 :
                if x==x235 and y==y235 or x==x235 and y==y235:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=236 :
                if x==x236 and y==y236 or x==x236 and y==y236:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=237 :
                if x==x237 and y==y237 or x==x237 and y==y237:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=238 :
                if x==x238 and y==y238 or x==x238 and y==y238:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=239 :
                if x==x239 and y==y239 or x==x239 and y==y239:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=240 :
                if x==x240 and y==y240 or x==x240 and y==y240:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=241 :
                if x==x241 and y==y241 or x==x241 and y==y241:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=242 :
                if x==x242 and y==y242 or x==x242 and y==y242:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=243 :
                if x==x243 and y==y243 or x==x243 and y==y243:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=244 :
                if x==x244 and y==y244 or x==x244 and y==y244:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=245 :
                if x==x245 and y==y245 or x==x245 and y==y245:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=246 :
                if x==x246 and y==y246 or x==x246 and y==y246:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=247 :
                if x==x247 and y==y247 or x==x247 and y==y247:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=248 :
                if x==x248 and y==y248 or x==x248 and y==y248:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=249 :
                if x==x249 and y==y249 or x==x249 and y==y249:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=250 :
                if x==x250 and y==y250 or x==x250 and y==y250:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=251 :
                if x==x251 and y==y251 or x==x251 and y==y251:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=252 :
                if x==x252 and y==y252 or x==x252 and y==y252:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=253 :
                if x==x253 and y==y253 or x==x253 and y==y253:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=254 :
                if x==x254 and y==y254 or x==x254 and y==y254:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=255 :
                if x==x255 and y==y255 or x==x255 and y==y255:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=256 :
                if x==x256 and y==y256 or x==x256 and y==y256:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=257 :
                if x==x257 and y==y257 or x==x257 and y==y257:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=258 :
                if x==x258 and y==y258 or x==x258 and y==y258:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=259 :
                if x==x259 and y==y259 or x==x259 and y==y259:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=260 :
                if x==x260 and y==y260 or x==x260 and y==y260:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=261 :
                if x==x261 and y==y261 or x==x261 and y==y261:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=262 :
                if x==x262 and y==y262 or x==x262 and y==y262:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=263 :
                if x==x263 and y==y263 or x==x263 and y==y263:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=264 :
                if x==x264 and y==y264 or x==x264 and y==y264:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=265 :
                if x==x265 and y==y265 or x==x265 and y==y265:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=266 :
                if x==x266 and y==y266 or x==x266 and y==y266:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=267 :
                if x==x267 and y==y267 or x==x267 and y==y267:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=268 :
                if x==x268 and y==y268 or x==x268 and y==y268:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=269 :
                if x==x269 and y==y269 or x==x269 and y==y269:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=270 :
                if x==x270 and y==y270 or x==x270 and y==y270:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=271 :
                if x==x271 and y==y271 or x==x271 and y==y271:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=272 :
                if x==x272 and y==y272 or x==x272 and y==y272:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=273 :
                if x==x273 and y==y273 or x==x273 and y==y273:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=274 :
                if x==x274 and y==y274 or x==x274 and y==y274:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=275 :
                if x==x275 and y==y275 or x==x275 and y==y275:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=276 :
                if x==x276 and y==y276 or x==x276 and y==y276:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=277 :
                if x==x277 and y==y277 or x==x277 and y==y277:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=278 :
                if x==x278 and y==y278 or x==x278 and y==y278:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=279 :
                if x==x279 and y==y279 or x==x279 and y==y279:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=280 :
                if x==x280 and y==y280 or x==x280 and y==y280:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=281 :
                if x==x281 and y==y281 or x==x281 and y==y281:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=282 :
                if x==x282 and y==y282 or x==x282 and y==y282:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=283 :
                if x==x283 and y==y283 or x==x283 and y==y283:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=284 :
                if x==x284 and y==y284 or x==x284 and y==y284:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=285 :
                if x==x285 and y==y285 or x==x285 and y==y285:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=286 :
                if x==x286 and y==y286 or x==x286 and y==y286:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=287 :
                if x==x287 and y==y287 or x==x287 and y==y287:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=288 :
                if x==x288 and y==y288 or x==x288 and y==y288:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=289 :
                if x==x289 and y==y289 or x==x289 and y==y289:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=290 :
                if x==x290 and y==y290 or x==x290 and y==y290:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=291 :
                if x==x291 and y==y291 or x==x291 and y==y291:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=292 :
                if x==x292 and y==y292 or x==x292 and y==y292:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=293 :
                if x==x293 and y==y293 or x==x293 and y==y293:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=294 :
                if x==x294 and y==y294 or x==x294 and y==y294:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=295 :
                if x==x295 and y==y295 or x==x295 and y==y295:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=296 :
                if x==x296 and y==y296 or x==x296 and y==y296:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=297 :
                if x==x297 and y==y297 or x==x297 and y==y297:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=298 :
                if x==x298 and y==y298 or x==x298 and y==y298:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=299 :
                if x==x299 and y==y299 or x==x299 and y==y299:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=300 :
                if x==x300 and y==y300 or x==x300 and y==y300:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=301 :
                if x==x301 and y==y301 or x==x301 and y==y301:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=302 :
                if x==x302 and y==y302 or x==x302 and y==y302:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=303 :
                if x==x303 and y==y303 or x==x303 and y==y303:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=304 :
                if x==x304 and y==y304 or x==x304 and y==y304:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=305 :
                if x==x305 and y==y305 or x==x305 and y==y305:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=306 :
                if x==x306 and y==y306 or x==x306 and y==y306:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=307 :
                if x==x307 and y==y307 or x==x307 and y==y307:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=308 :
                if x==x308 and y==y308 or x==x308 and y==y308:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=309 :
                if x==x309 and y==y309 or x==x309 and y==y309:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=310 :
                if x==x310 and y==y310 or x==x310 and y==y310:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=311 :
                if x==x311 and y==y311 or x==x311 and y==y311:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=312 :
                if x==x312 and y==y312 or x==x312 and y==y312:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=313 :
                if x==x313 and y==y313 or x==x313 and y==y313:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=314 :
                if x==x314 and y==y314 or x==x314 and y==y314:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=315 :
                if x==x315 and y==y315 or x==x315 and y==y315:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=316 :
                if x==x316 and y==y316 or x==x316 and y==y316:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=317 :
                if x==x317 and y==y317 or x==x317 and y==y317:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=318 :
                if x==x318 and y==y318 or x==x318 and y==y318:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=319 :
                if x==x319 and y==y319 or x==x319 and y==y319:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=320 :
                if x==x320 and y==y320 or x==x320 and y==y320:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=321 :
                if x==x321 and y==y321 or x==x321 and y==y321:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=322 :
                if x==x322 and y==y322 or x==x322 and y==y322:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=323 :
                if x==x323 and y==y323 or x==x323 and y==y323:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=324 :
                if x==x324 and y==y324 or x==x324 and y==y324:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=325 :
                if x==x325 and y==y325 or x==x325 and y==y325:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=326 :
                if x==x326 and y==y326 or x==x326 and y==y326:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=327 :
                if x==x327 and y==y327 or x==x327 and y==y327:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=328 :
                if x==x328 and y==y328 or x==x328 and y==y328:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=329 :
                if x==x329 and y==y329 or x==x329 and y==y329:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=330 :
                if x==x330 and y==y330 or x==x330 and y==y330:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=331 :
                if x==x331 and y==y331 or x==x331 and y==y331:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=332 :
                if x==x332 and y==y332 or x==x332 and y==y332:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=333 :
                if x==x333 and y==y333 or x==x333 and y==y333:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=334 :
                if x==x334 and y==y334 or x==x334 and y==y334:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=335 :
                if x==x335 and y==y335 or x==x335 and y==y335:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=336 :
                if x==x336 and y==y336 or x==x336 and y==y336:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=337 :
                if x==x337 and y==y337 or x==x337 and y==y337:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=338 :
                if x==x338 and y==y338 or x==x338 and y==y338:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=339 :
                if x==x339 and y==y339 or x==x339 and y==y339:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=340 :
                if x==x340 and y==y340 or x==x340 and y==y340:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=341 :
                if x==x341 and y==y341 or x==x341 and y==y341:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=342 :
                if x==x342 and y==y342 or x==x342 and y==y342:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=343 :
                if x==x343 and y==y343 or x==x343 and y==y343:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=344 :
                if x==x344 and y==y344 or x==x344 and y==y344:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=345 :
                if x==x345 and y==y345 or x==x345 and y==y345:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=346 :
                if x==x346 and y==y346 or x==x346 and y==y346:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=347 :
                if x==x347 and y==y347 or x==x347 and y==y347:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=348 :
                if x==x348 and y==y348 or x==x348 and y==y348:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=349 :
                if x==x349 and y==y349 or x==x349 and y==y349:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=350 :
                if x==x350 and y==y350 or x==x350 and y==y350:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=351 :
                if x==x351 and y==y351 or x==x351 and y==y351:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=352 :
                if x==x352 and y==y352 or x==x352 and y==y352:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=353 :
                if x==x353 and y==y353 or x==x353 and y==y353:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=354 :
                if x==x354 and y==y354 or x==x354 and y==y354:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=355 :
                if x==x355 and y==y355 or x==x355 and y==y355:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=356 :
                if x==x356 and y==y356 or x==x356 and y==y356:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=357 :
                if x==x357 and y==y357 or x==x357 and y==y357:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=358 :
                if x==x358 and y==y358 or x==x358 and y==y358:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=359 :
                if x==x359 and y==y359 or x==x359 and y==y359:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=360 :
                if x==x360 and y==y360 or x==x360 and y==y360:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=361 :
                if x==x361 and y==y361 or x==x361 and y==y361:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=362 :
                if x==x362 and y==y362 or x==x362 and y==y362:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=363 :
                if x==x363 and y==y363 or x==x363 and y==y363:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=364 :
                if x==x364 and y==y364 or x==x364 and y==y364:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=365 :
                if x==x365 and y==y365 or x==x365 and y==y365:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=366 :
                if x==x366 and y==y366 or x==x366 and y==y366:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=367 :
                if x==x367 and y==y367 or x==x367 and y==y367:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=368 :
                if x==x368 and y==y368 or x==x368 and y==y368:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=369 :
                if x==x369 and y==y369 or x==x369 and y==y369:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=370 :
                if x==x370 and y==y370 or x==x370 and y==y370:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=371 :
                if x==x371 and y==y371 or x==x371 and y==y371:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=372 :
                if x==x372 and y==y372 or x==x372 and y==y372:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=373 :
                if x==x373 and y==y373 or x==x373 and y==y373:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=374 :
                if x==x374 and y==y374 or x==x374 and y==y374:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=375 :
                if x==x375 and y==y375 or x==x375 and y==y375:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=376 :
                if x==x376 and y==y376 or x==x376 and y==y376:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=377 :
                if x==x377 and y==y377 or x==x377 and y==y377:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=378 :
                if x==x378 and y==y378 or x==x378 and y==y378:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=379 :
                if x==x379 and y==y379 or x==x379 and y==y379:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=380 :
                if x==x380 and y==y380 or x==x380 and y==y380:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=381 :
                if x==x381 and y==y381 or x==x381 and y==y381:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=382 :
                if x==x382 and y==y382 or x==x382 and y==y382:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=383 :
                if x==x383 and y==y383 or x==x383 and y==y383:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=384 :
                if x==x384 and y==y384 or x==x384 and y==y384:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=385 :
                if x==x385 and y==y385 or x==x385 and y==y385:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=386 :
                if x==x386 and y==y386 or x==x386 and y==y386:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=387 :
                if x==x387 and y==y387 or x==x387 and y==y387:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=388 :
                if x==x388 and y==y388 or x==x388 and y==y388:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=389 :
                if x==x389 and y==y389 or x==x389 and y==y389:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=390 :
                if x==x390 and y==y390 or x==x390 and y==y390:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=391 :
                if x==x391 and y==y391 or x==x391 and y==y391:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=392 :
                if x==x392 and y==y392 or x==x392 and y==y392:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=393 :
                if x==x393 and y==y393 or x==x393 and y==y393:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=394 :
                if x==x394 and y==y394 or x==x394 and y==y394:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=395 :
                if x==x395 and y==y395 or x==x395 and y==y395:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=396 :
                if x==x396 and y==y396 or x==x396 and y==y396:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=397 :
                if x==x397 and y==y397 or x==x397 and y==y397:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=398 :
                if x==x398 and y==y398 or x==x398 and y==y398:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=399 :
                if x==x399 and y==y399 or x==x399 and y==y399:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=400 :
                if x==x400 and y==y400 or x==x400 and y==y400:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=401 :
                if x==x401 and y==y401 or x==x401 and y==y401:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=402 :
                if x==x402 and y==y402 or x==x402 and y==y402:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=403 :
                if x==x403 and y==y403 or x==x403 and y==y403:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=404 :
                if x==x404 and y==y404 or x==x404 and y==y404:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=405 :
                if x==x405 and y==y405 or x==x405 and y==y405:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=406 :
                if x==x406 and y==y406 or x==x406 and y==y406:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=407 :
                if x==x407 and y==y407 or x==x407 and y==y407:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=408 :
                if x==x408 and y==y408 or x==x408 and y==y408:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=409 :
                if x==x409 and y==y409 or x==x409 and y==y409:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=410 :
                if x==x410 and y==y410 or x==x410 and y==y410:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=411 :
                if x==x411 and y==y411 or x==x411 and y==y411:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=412 :
                if x==x412 and y==y412 or x==x412 and y==y412:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=413 :
                if x==x413 and y==y413 or x==x413 and y==y413:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=414 :
                if x==x414 and y==y414 or x==x414 and y==y414:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=415 :
                if x==x415 and y==y415 or x==x415 and y==y415:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=416 :
                if x==x416 and y==y416 or x==x416 and y==y416:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=417 :
                if x==x417 and y==y417 or x==x417 and y==y417:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=418 :
                if x==x418 and y==y418 or x==x418 and y==y418:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=419 :
                if x==x419 and y==y419 or x==x419 and y==y419:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=420 :
                if x==x420 and y==y420 or x==x420 and y==y420:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=421 :
                if x==x421 and y==y421 or x==x421 and y==y421:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=422 :
                if x==x422 and y==y422 or x==x422 and y==y422:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=423 :
                if x==x423 and y==y423 or x==x423 and y==y423:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=424 :
                if x==x424 and y==y424 or x==x424 and y==y424:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=425 :
                if x==x425 and y==y425 or x==x425 and y==y425:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=426 :
                if x==x426 and y==y426 or x==x426 and y==y426:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=427 :
                if x==x427 and y==y427 or x==x427 and y==y427:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=428 :
                if x==x428 and y==y428 or x==x428 and y==y428:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=429 :
                if x==x429 and y==y429 or x==x429 and y==y429:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=430 :
                if x==x430 and y==y430 or x==x430 and y==y430:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=431 :
                if x==x431 and y==y431 or x==x431 and y==y431:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=432 :
                if x==x432 and y==y432 or x==x432 and y==y432:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=433 :
                if x==x433 and y==y433 or x==x433 and y==y433:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=434 :
                if x==x434 and y==y434 or x==x434 and y==y434:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=435 :
                if x==x435 and y==y435 or x==x435 and y==y435:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=436 :
                if x==x436 and y==y436 or x==x436 and y==y436:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=437 :
                if x==x437 and y==y437 or x==x437 and y==y437:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=438 :
                if x==x438 and y==y438 or x==x438 and y==y438:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=439 :
                if x==x439 and y==y439 or x==x439 and y==y439:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=440 :
                if x==x440 and y==y440 or x==x440 and y==y440:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=441 :
                if x==x441 and y==y441 or x==x441 and y==y441:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=442 :
                if x==x442 and y==y442 or x==x442 and y==y442:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=443 :
                if x==x443 and y==y443 or x==x443 and y==y443:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=444 :
                if x==x444 and y==y444 or x==x444 and y==y444:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=445 :
                if x==x445 and y==y445 or x==x445 and y==y445:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=446 :
                if x==x446 and y==y446 or x==x446 and y==y446:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=447 :
                if x==x447 and y==y447 or x==x447 and y==y447:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=448 :
                if x==x448 and y==y448 or x==x448 and y==y448:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=449 :
                if x==x449 and y==y449 or x==x449 and y==y449:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=450 :
                if x==x450 and y==y450 or x==x450 and y==y450:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=451 :
                if x==x451 and y==y451 or x==x451 and y==y451:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=452 :
                if x==x452 and y==y452 or x==x452 and y==y452:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=453 :
                if x==x453 and y==y453 or x==x453 and y==y453:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=454 :
                if x==x454 and y==y454 or x==x454 and y==y454:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=455 :
                if x==x455 and y==y455 or x==x455 and y==y455:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=456 :
                if x==x456 and y==y456 or x==x456 and y==y456:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=457 :
                if x==x457 and y==y457 or x==x457 and y==y457:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=458 :
                if x==x458 and y==y458 or x==x458 and y==y458:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=459 :
                if x==x459 and y==y459 or x==x459 and y==y459:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=460 :
                if x==x460 and y==y460 or x==x460 and y==y460:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=461 :
                if x==x461 and y==y461 or x==x461 and y==y461:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=462 :
                if x==x462 and y==y462 or x==x462 and y==y462:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=463 :
                if x==x463 and y==y463 or x==x463 and y==y463:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=464 :
                if x==x464 and y==y464 or x==x464 and y==y464:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=465 :
                if x==x465 and y==y465 or x==x465 and y==y465:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=466 :
                if x==x466 and y==y466 or x==x466 and y==y466:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=467 :
                if x==x467 and y==y467 or x==x467 and y==y467:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=468 :
                if x==x468 and y==y468 or x==x468 and y==y468:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=469 :
                if x==x469 and y==y469 or x==x469 and y==y469:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=470 :
                if x==x470 and y==y470 or x==x470 and y==y470:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=471 :
                if x==x471 and y==y471 or x==x471 and y==y471:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=472 :
                if x==x472 and y==y472 or x==x472 and y==y472:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=473 :
                if x==x473 and y==y473 or x==x473 and y==y473:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=474 :
                if x==x474 and y==y474 or x==x474 and y==y474:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=475 :
                if x==x475 and y==y475 or x==x475 and y==y475:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=476 :
                if x==x476 and y==y476 or x==x476 and y==y476:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=477 :
                if x==x477 and y==y477 or x==x477 and y==y477:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=478 :
                if x==x478 and y==y478 or x==x478 and y==y478:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=479 :
                if x==x479 and y==y479 or x==x479 and y==y479:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=480 :
                if x==x480 and y==y480 or x==x480 and y==y480:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=481 :
                if x==x481 and y==y481 or x==x481 and y==y481:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=482 :
                if x==x482 and y==y482 or x==x482 and y==y482:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=483 :
                if x==x483 and y==y483 or x==x483 and y==y483:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        if isz>=484 :
                if x==x484 and y==y484 or x==x484 and y==y484:
                    dx=dx+8000
                    dy=dy+8000
                    Image2Canevas=monCanevas.create_image(320,360,image=gameover)
                    music=0
        mafenetre.after(150,animation)

#le serpent disparait quand le joueur touche les bords (envoyé en 8000, 8000)
def testBords(x,y,dx,dy):
        global music
        if x>640 or x<-10:
            dx=dx+8000
            dy=dy+8000
            Image2Canevas=monCanevas.create_image(320,360,image=gameover)
            music=0
        if y>640 or y<-10:
            dx=dx+8000
            dy=dy+8000
            Image2Canevas=monCanevas.create_image(320,360,image=gameover)
            music=0
        return dx,dy

#les sons et musiques
def croc():
    croque.play()

def megalovania():
    musique.play()

def lost():
    over.play()


def effacer():
	programme=0

# Création de la fenetre principal(main windox)
mafenetre=Tk()
mafenetre.title("Damier")
mafenetre.geometry("720x720")

#Création du widghet Canevas et de sa couleur
monCanevas=Canvas(mafenetre,bg="#3A9D23",height=655,width=655)
monCanevas.pack(side=RIGHT,padx=5,pady=5)

#importation des sons et musiques
croque=pygame.mixer.Sound("croc.ogg")
musique=pygame.mixer.Sound("megalovania.ogg")
over=pygame.mixer.Sound("lost.ogg")

#importation des images
pomme=PhotoImage(file="pomme.png")
gameover=PhotoImage(file="GameOver.png")

damier()

#creation des carré
Image1Canevas=monCanevas.create_image(a,b,image=pomme)
balle=monCanevas.create_rectangle(330,300,360,330,fill='red')
balle1=monCanevas.create_rectangle(330,300,360,330,fill='blue')
balle2=monCanevas.create_rectangle(330,300,360,330,fill='blue')
balle3=monCanevas.create_rectangle(330,300,360,330,fill='blue')
balle4=monCanevas.create_rectangle(330,300,360,330,fill='blue')
balle5=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle6=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle7=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle8=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle9=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle10=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle11=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle12=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle13=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle14=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle15=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle16=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle17=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle18=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle19=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle20=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle21=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle22=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle23=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle24=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle25=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle26=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle27=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle28=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle29=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle30=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle31=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle32=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle33=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle34=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle35=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle36=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle37=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle38=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle39=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle40=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle41=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle42=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle43=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle44=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle45=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle46=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle47=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle48=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle49=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle50=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle51=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle52=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle53=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle54=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle55=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle56=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle57=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle58=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle59=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle60=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle61=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle62=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle63=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle64=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle65=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle66=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle67=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle68=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle69=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle70=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle71=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle72=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle73=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle74=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle75=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle76=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle77=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle78=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle79=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle80=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle81=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle82=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle83=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle84=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle85=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle86=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle87=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle88=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle89=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle90=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle91=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle92=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle93=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle94=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle95=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle96=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle97=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle98=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle99=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle100=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle101=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle102=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle103=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle104=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle105=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle106=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle107=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle108=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle109=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle110=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle111=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle112=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle113=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle114=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle115=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle116=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle117=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle118=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle119=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle120=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle121=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle122=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle123=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle124=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle125=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle126=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle127=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle128=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle129=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle130=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle131=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle132=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle133=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle134=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle135=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle136=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle137=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle138=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle139=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle140=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle141=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle142=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle143=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle144=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle145=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle146=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle147=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle148=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle149=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle150=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle151=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle152=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle153=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle154=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle155=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle156=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle157=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle158=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle159=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle160=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle161=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle162=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle163=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle164=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle165=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle166=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle167=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle168=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle169=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle170=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle171=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle172=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle173=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle174=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle175=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle176=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle177=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle178=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle179=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle180=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle181=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle182=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle183=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle184=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle185=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle186=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle187=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle188=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle189=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle190=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle191=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle192=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle193=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle194=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle195=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle196=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle197=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle198=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle199=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle200=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle201=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle202=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle203=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle204=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle205=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle206=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle207=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle208=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle209=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle210=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle211=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle212=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle213=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle214=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle215=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle216=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle217=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle218=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle219=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle220=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle221=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle222=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle223=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle224=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle225=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle226=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle227=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle228=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle229=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle230=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle231=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle232=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle233=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle234=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle235=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle236=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle237=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle238=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle239=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle240=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle241=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle242=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle243=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle244=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle245=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle246=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle247=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle248=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle249=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle250=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle251=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle252=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle253=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle254=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle255=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle256=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle257=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle258=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle259=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle260=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle261=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle262=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle263=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle264=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle265=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle266=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle267=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle268=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle269=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle270=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle271=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle272=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle273=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle274=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle275=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle276=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle277=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle278=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle279=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle280=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle281=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle282=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle283=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle284=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle285=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle286=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle287=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle288=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle289=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle290=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle291=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle292=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle293=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle294=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle295=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle296=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle297=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle298=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle299=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle300=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle301=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle302=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle303=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle304=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle305=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle306=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle307=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle308=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle309=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle310=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle311=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle312=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle313=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle314=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle315=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle316=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle317=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle318=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle319=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle320=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle321=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle322=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle323=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle324=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle325=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle326=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle327=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle328=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle329=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle330=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle331=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle332=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle333=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle334=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle335=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle336=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle337=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle338=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle339=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle340=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle341=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle342=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle343=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle344=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle345=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle346=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle347=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle348=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle349=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle350=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle351=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle352=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle353=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle354=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle355=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle356=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle357=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle358=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle359=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle360=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle361=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle362=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle363=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle364=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle365=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle366=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle367=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle368=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle369=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle370=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle371=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle372=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle373=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle374=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle375=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle376=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle377=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle378=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle379=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle380=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle381=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle382=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle383=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle384=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle385=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle386=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle387=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle388=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle389=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle390=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle391=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle392=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle393=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle394=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle395=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle396=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle397=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle398=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle399=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle400=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle401=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle402=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle403=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle404=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle405=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle406=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle407=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle408=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle409=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle410=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle411=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle412=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle413=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle414=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle415=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle416=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle417=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle418=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle419=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle420=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle421=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle422=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle423=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle424=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle425=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle426=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle427=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle428=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle429=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle430=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle431=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle432=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle433=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle434=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle435=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle436=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle437=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle438=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle439=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle440=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle441=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle442=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle443=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle444=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle445=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle446=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle447=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle448=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle449=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle450=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle451=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle452=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle453=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle454=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle455=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle456=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle457=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle458=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle459=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle460=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle461=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle462=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle463=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle464=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle465=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle466=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle467=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle468=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle469=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle470=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle471=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle472=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle473=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle474=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle475=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle476=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle477=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle478=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle479=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle480=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle481=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle482=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle483=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')
balle484=monCanevas.create_rectangle(330+8000,300+8000,360+8000,330+8000,fill='blue')

#creation du boutton demarer
Button(mafenetre,text="Démarrer",command=animation).pack(side=LEFT,padx=0,pady=0)
Button(mafenetre,text="Reset", command=effacer).pack(side=LEFT,padx=0,pady=0)


monCanevas.bind("<Key>",z)
monCanevas.focus_set()
mafenetre.mainloop()
pygame.mixer.quit()