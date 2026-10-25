import tempfile,unittest
from pathlib import Path
from main import plan_moves,apply_moves
class OrganizerTests(unittest.TestCase):
    def test_plan_does_not_move(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"a.TXT"; p.write_text("x")
            plan=plan_moves(d); self.assertEqual(len(plan),1); self.assertTrue(p.exists())
    def test_apply_moves(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"a.txt"; p.write_text("x")
            moved=apply_moves(plan_moves(d)); self.assertEqual(len(moved),1); self.assertTrue((Path(d)/"txt"/"a.txt").exists())
if __name__=="__main__": unittest.main()
