import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("summarize", Path(__file__).parents[1] / "scripts" / "summarize.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def observation(question="q1", status="completed", mention="no", citations="available", url=""):
    return {"question_id": question, "response_status": status, "brand_mention": mention,
            "citation_status": citations, "own_citation_url": url}


class MeasurementSemantics(unittest.TestCase):
    def test_failure_and_unknown_are_not_negative_mentions(self):
        result = module.summarize([observation(mention="yes"), observation(status="failed", mention="unknown"), observation(mention="unknown")])
        self.assertEqual(result["answer_mention_rate"], {"numerator": 1, "denominator": 1, "percent": 100.0})
        self.assertEqual(result["failed_or_missing_answers"], 1)
        self.assertEqual(result["unknown_mention_answers"], 1)

    def test_answer_rate_differs_from_question_coverage(self):
        result = module.summarize([observation(mention="yes"), observation(), observation()])
        self.assertEqual(result["answer_mention_rate"]["denominator"], 3)
        self.assertEqual(result["question_coverage"]["denominator"], 1)

    def test_empty_sources_differ_from_unavailable_sources(self):
        result = module.summarize([observation(url="https://example.com/"), observation(), observation(citations="unavailable")])
        self.assertEqual(result["owned_citation_rate"], {"numerator": 1, "denominator": 2, "percent": 50.0})

    def test_empty_sample_has_no_invented_zero_percentage(self):
        self.assertIsNone(module.summarize([])["answer_mention_rate"]["percent"])

    def test_contradictory_observation_is_rejected(self):
        with self.assertRaises(ValueError):
            module.summarize([observation(status="failed", mention="no")])


if __name__ == "__main__":
    unittest.main()
